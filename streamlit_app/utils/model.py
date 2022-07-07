import pandas as pd
from transformers import AutoTokenizer, TFAutoModelForCausalLM
import tensorflow as tf
import unicodedata
import re
import os

def predict_next_word_df(sentence, tokenizer, model, n_word=1, startwith='', list_tokens=None, format_list=False):
    #Preparation de la liste de mots
    if list_tokens == None:
        list_tokens = make_list_tokens(tokenizer)
        
    inputs = tokenizer(sentence, return_tensors="tf")
    is_empty = tf.equal(tf.size(inputs["input_ids"]),0).numpy()
    if is_empty:
        inputs = tokenizer("the", return_tensors="tf")
    outputs = model(inputs)
    predictions = outputs[0]
    pred = predictions[0][-1]
    result = pd.DataFrame({"Proba":pred.numpy(),"Word":list_tokens})
    result = result[result["Word"].str.startswith(startwith)]
    result = result.drop_duplicates(subset="Word")
    result = result.sort_values(by="Proba", ascending=False).head(n_word)
    
    if format_list:
        result = result["Word"].tolist()
    return result

def score_sentence(sentence, tokenizer, model, n_word=1, verbose=False, list_tokens=None):
    #Preparation de la liste de mots
    if list_tokens == None:
        list_tokens = make_list_tokens(tokenizer)
        
    sen_split = sentence.split()
    context = sen_split[0]
    score = 0
    letter = 0
    for i in range(1, len(sen_split)):
        #word = " "+sen_split[i] #Ajoute un espcace au début du mot pour le tokenizateur
        word = sen_split[i] #Ajoute un espcace au début du mot pour le tokenizateur
        letter += (len(sen_split[i]))
        found = False
        j = 0
        startwith = ""
        while j < len(word) and found==False:
            startwith += word[j]
            pred = predict_next_word_df(context, tokenizer, model, n_word, startwith=startwith, list_tokens=list_tokens, format_list=True)
            if verbose:
                print("Context:", context, "--Start with:", startwith, "--Prediction:", pred)
            if word in pred:
                found = True
                score += (len(sen_split[i]) - j )
            if not pred:
                break
            j += 1
        context += word
    return score, letter

def load_tokenizer_and_model():
    tokenizer_path = os.path.join(os.path.abspath(".."),"models", "GPT2_tokenizer_40000")
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
    list_tokens = make_list_tokens(tokenizer)
    model_path = os.path.join(os.path.abspath(".."),"models", "GPT2_model_40000")
    model = TFAutoModelForCausalLM.from_pretrained(model_path)
    return tokenizer,list_tokens, model

def unicode_to_ascii(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn')

def clean_sentences(l):
    # nettoyage de la phase
    l = unicode_to_ascii(l.lower())
    l = re.sub(r"([?!,¿.])", r" \1 ", l)
    l = re.sub(r'[" "]+', " ", l)
    
    # decontraction
    l = re.sub(r"won't", "will not", l)
    l = re.sub(r"can\'t", "can not", l)
    l = re.sub(r"n\'t", " not", l)
    l = re.sub(r"\'re", " are", l)
    l = re.sub(r"\'d", " would", l)
    l = re.sub(r"\'ll", " will", l)
    l = re.sub(r"\'t", " not", l)
    l = re.sub(r"\'ve", " have", l)
    l = re.sub(r"\'m", " am", l)
    
    # replacing everything with space except (a-z, A-Z, ".", "?", "!", ",")
    #l = re.sub(r"[^a-z?.!;]+", " ", l)
    l = re.sub(r"[^a-z]+", " ", l)
    return l

def split_sentence(sentence):
    sen_split = sentence.split()
    if sentence[-1] == " ":
        startwith = ""
        sentence = " ".join(sen_split)
    else:
        #startwith = " "+sen_split[-1]
        startwith = sen_split[-1]
        sentence = " ".join(sen_split[:-1])
    return sentence, startwith

def score_mot(context, mot, tokenizer, model, list_tokens=None, n_word=1):
    if list_tokens == None:
        list_tokens = make_list_tokens(tokenizer)
    startwith = ""
    letter = len(mot)
    for i in range(len(mot)):
        pred = predict_next_word_df(context, tokenizer, model, n_word, startwith=startwith, list_tokens=list_tokens, format_list=True)
        startwith += mot[i]
        if not pred:
            return (mot, 0, letter) # Si il n'y a aucune suggestion avec n lettres, il n'y en aura pas avec n+1
        if mot in pred:
            return (mot, letter-i, letter) # Renvois le score du mot
    return (mot, 0, letter) # Si le mot n'est pas trouvé jusqu'a la fin renvois un score de 0

def score_sentence_annotated(sentence, tokenizer, model, list_tokens=None, n_word=1):
    #Preparation de la liste de mots
    if list_tokens == None:
        list_tokens = make_list_tokens(tokenizer)
    sen_split = sentence.split()
    context = sen_split[0]
    result = [(sen_split[0],0,0)]
    for mot in sen_split[1:]:
        result.append(score_mot(context, mot, tokenizer=tokenizer, model=model, list_tokens=list_tokens, n_word=n_word))
        context += " "
        context += mot
    return result

def annotated_mot(annotated_score):
    mot = annotated_score[0] + " "
    score = str(annotated_score[1])+"/"+str(annotated_score[2])
    r = int(255*(1-(annotated_score[1]/annotated_score[2])))
    g = int(255*((annotated_score[1]/annotated_score[2])))
    color = "rgb("+str(r)+", "+str(g)+", 0)"
    return (mot, score, color)

def annotated_score(sentence, tokenizer, model, list_tokens=None, n_word=1):
    #Preparation de la liste de mots
    if list_tokens == None:
        list_tokens = make_list_tokens(tokenizer)
    tuples = score_sentence_annotated(sentence, tokenizer, model, list_tokens, n_word)
    results = [(tuples[0][0]+ " ", "", "rgb(255, 255, 255)")]
    for mot in tuples[1:]:
        results.append(annotated_mot(mot))
    return results

def make_list_tokens(tokenizer):
    list_tokens = [None]*tokenizer.vocab_size
    for i in range(0,tokenizer.vocab_size):
        list_tokens[i]=tokenizer.decode([i]).strip()
    list_tokens[0] = "."
    return list_tokens