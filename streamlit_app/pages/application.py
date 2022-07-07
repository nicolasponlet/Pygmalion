import streamlit as st
from utils.utils import v_spacer, percent_bar, pie_score, image_path
from PIL import Image
import utils.model as GPT2
import matplotlib.pyplot as plt
from annotated_text import annotated_text
import tensorflow as tf
import pandas as pd
import os

# @st.cache
def app():
    col1,col2 = st.columns([1,2])
    original1 = Image.open(image_path("Pygmalion_logo.jpg"))
    col1.image(original1, use_column_width=True)

    col2.title("Pygmalion")
    col2.header("Démo de l'application")
    v_spacer(2)

    tokenizer_GPT2, list_tokens, model_GPT2 = GPT2.load_tokenizer_and_model()
    if 'message_text' not in st.session_state:
        st.session_state.message_text = ''
    if 'slider_val' not in st.session_state:
        st.session_state.slider_val = 3
    if 'pred_score' not in st.session_state:
        st.session_state.pred_score = 0
    if 'submitted' not in locals():
        submitted = False

    # Test la présence de GPU
    listGPU = tf.config.list_physical_devices('GPU')
    if not listGPU: #listGPU empty = False
        st.warning("Aucun GPU n'a été détécté : les calculs seront très long!")
    
    # Affiche deux bouttons pour remplir automatiquement le message avec une phrase du dataset de validation ou une phrase prise sur wikipedia
    col1, col2 = st.columns(2)
    with col1:
        text_help = "Sélectionne aléatoirement une phrase du dataset de validation d’ENRON."
        if st.button("Phrase aléatoire ENRON", help=text_help):
            file = os.path.join(os.path.abspath(".."),"models", "sentences.csv")
            df = pd.read_csv(file)
            sentence = df[df.source=="ENRON"].sample()
            st.session_state.message_text = sentence["sentence"].item()
    
    with col2:
        text_help = "Sélectionne aléatoirement une phrase de Wikipédia. Les phrases ne sont pas lié à la thématique de l’énergie et permettent de mesurer la généralisation du modèle."
        if st.button("Phrase aléatoire wikipedia", help=text_help):
            file = os.path.join(os.path.abspath(".."),"models", "sentences.csv")
            df = pd.read_csv(file)
            sentence = df[df.source=="wiki"].sample()
            st.session_state.message_text = sentence["sentence"].item()
    txt, slider_val, pred_score, submitted = body(st.session_state.message_text, st.session_state.slider_val, st.session_state.pred_score)
    
    st.session_state.message_text = txt
    st.session_state.slider_val = slider_val
    if pred_score == 'Prédiction': #Change radio buton to position value
        st.session_state.pred_score = 0
    elif pred_score == 'Score':
        st.session_state.pred_score = 1
    if submitted:
        if len(st.session_state.message_text.split()) < 1:
                st.warning('Veuillez renseigner au moins un mot')
        else:
            if st.session_state.pred_score == 0:
                if is_multiple_sentences(st.session_state.message_text):
                    st.warning('Ce modèle a été entrainé par phrase et sera moins efficace sur des paragraphes plus long.')
                predict_container(tokenizer_GPT2, model_GPT2, list_tokens)
            else:
                if is_multiple_sentences(st.session_state.message_text):
                    st.warning('Ce modèle a été entrainé par phrase et sera moins efficace sur des paragraphes plus long.')
                score_container(tokenizer_GPT2, model_GPT2)
        
def body(txt, slider_val, pred_score):
    body=st.form("body")
    txt_v = body.text_area("Message", txt, height = 100, placeholder='Veuillez écrire le texte ici')
    text_help = "Nombre de suggestions renvoyé par le modèle. Plus ce nombre est important et plus le modèle à de chance de trouver le mot souhaité mais plus l'utilisateur devra lire de suggestions."
    slider_val_v = body.slider("Nombre de suggestions", min_value = 1, max_value=10, value=slider_val, step=1, help=text_help)
    text_help = "Souhaitez-vous prédire le prochain mot ou calculer le score du modèle pour la phrase que vous avez renseigné?"
    pred_score_v = body.radio("Prédiction du mot suivant ou calcul du score du model ?", ('Prédiction', 'Score'), index=pred_score, help=text_help)
    submitted = False
    if body.form_submit_button("Submit"):
        submitted = True
        return txt_v, slider_val_v, pred_score_v, submitted
    return txt, slider_val, pred_score, submitted        


def click_button(word, sentence):
    mots = sentence.split()
    mots.append(word)
    message_text =  " ".join(mots)
    message_text += " "
    st.session_state.message_text = message_text

def norm_proba(proba):
    proba = [0 if x < 0 else x for x in proba]
    sum_proba = sum(proba)
    if sum_proba == 0:
        return [0] * len(proba)
    else:
        return [ele/sum_proba for ele in proba]

def predict_container(tokenizer_GPT2, model_GPT2, list_tokens):
    container = st.container()
    container.write("Prédiction du mot suivant")
    clean_message = GPT2.clean_sentences(st.session_state.message_text)
    sentence, startwith = GPT2.split_sentence(clean_message)
    result = GPT2.predict_next_word_df(sentence, tokenizer_GPT2, model_GPT2, n_word=st.session_state.slider_val, startwith=startwith, list_tokens=list_tokens, format_list=False)
    word = result.Word.tolist()
    proba = result.Proba.tolist()
    proba = norm_proba(proba)
    nb_resultats = min(st.session_state.slider_val, len(word))
    if nb_resultats > 0:
        button_list = container.columns(nb_resultats)
        for i in range(nb_resultats):
            button_list[i].container()
            button_list[i].button(label = word[i], key = word[i], on_click=click_button, args=(word[i], sentence))
        container.pyplot(percent_bar(proba))
        if sum(proba) == 0:
            container.warning('Les probabilité calculé sont toutes très faible!')
    else:
        container.warning('Pas de résultat')
    return container

def score_container(tokenizer_GPT2, model_GPT2):
    container = st.container()
    clean_message = GPT2.clean_sentences(st.session_state.message_text)
    with st.spinner('Calcul du score'):
        at = GPT2.annotated_score(clean_message, tokenizer_GPT2, model_GPT2, n_word=st.session_state.slider_val)
        score = GPT2.score_sentence_annotated(clean_message, tokenizer_GPT2, model_GPT2, n_word=st.session_state.slider_val)

    container.write("Le score du nombre de lettres économisées est égal à la somme du score de chaque mot divisé par le nombre total de lettres. Il permet d’obtenir un ratio du nombre de lettres économisées.")
    if sum([ele[2] for ele in score]) == 0:
        st.warning('Il faut un minimum de deux mots pour calculer un score')
    else:
        score_sentence = sum([ele[1] for ele in score]) / sum([ele[2] for ele in score])
        container.pyplot(pie_score(score_sentence))
        annotated_text(*at)
        
    return container

def is_multiple_sentences(message_text):
    """
    Check if the message is composed by multiple sentence
    """
    if len(message_text.split("."))<=1:
        return False
    if len(message_text.split(".")[1]) == 0:
        return False
    return True