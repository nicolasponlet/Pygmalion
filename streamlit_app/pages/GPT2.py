
import streamlit as st
from utils.utils import v_spacer, image_path
from PIL import Image

# @st.cache
def app():
    col1,col2 = st.columns([1,2])
    original1 = Image.open(image_path("Pygmalion_logo.jpg"))
    col1.image(original1, use_column_width=True)

    col2.title("Le modèle GPT2")
    col2.header("Présentation du modèle")
    v_spacer(2) 
    
    st.markdown("""
    Annoncé en 2019 par [***OpenAI***](https://openai.com/blog/better-language-models/), GPT2 (Generative Pre-trained Transformer 2 ) est présenté comme un modèle universel
     en mesure de répondre à l'ensemble des problématiques du NLP :
     >- génération de texte
     >- comprehention de texte
     >- traduction automatique
     >- ...
     
     Le modèle GPT-2 est un modèle non supervisé. Il est qualifié de :
     >- ***Zero-shot learning*** : GPT2 ne nécessite pas d'entrainement, parce qu'il a été construit sur une base de plus de 8 millions de pages Web (40Go de texte), et comprend plus de 1,5 milliards de paramètres. Le dataset a été tokenizé suivant l'algorithme ***BPE*** (Byte Pair Encoding).
     >> On peut donc considérer que GPT2 couvre l'ensemble des données d'une langue et est considéré comme un ***"language model"***
     """
    )
    st.markdown("""
     >- ***Zero-shot setting*** : GPT2 n'a pas à être paramétré en fonction de la tâche à réaliser

     >> Pout plus d'informations quant à la structure et à l'entrainement de GPT2 voir le document publié par OpenAI, [“Language Models are Unsupervised Multitask Learners”](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
    """
    )
    st.markdown("\n GPT2 est distribué suivant plusieurs configurations")
    original = Image.open(image_path("GPT2_range.png"))
    st.image(original, use_column_width=True)
    original = Image.open(image_path("GPT2_struct.png"))
    st.image(original, use_column_width=True, caption="source: J.Alammar,The Illustrated GPT-2 (Visualizing Transformer Language Models)")
    st.markdown("""
    Pour les besoins de notre étude, nous avons choisi le modèle ***GPT-2 SMALL***, seul modèle compatible avec la puissance de calcul de nos ordinateurs personnels.
     Ce modèle s'appuie sur un dataset beaucoup plus petit. La notion de Zero-shot learning n'est plus applicable, pour obtenir de bons résultats il a été nécessaire de réaliser un ***"Fine tuning"*** de GPT2 sur la base du vocabulaire spécifique utilisé dans notre dataset.
    """
    )
    v_spacer(2)

    st.header("L'architecture de GPT2")
    st.markdown("""
    GPT2 est construit sur la base du modèle des ***Transformers*** tel que défini dans le document ["Attention is all you need"](https://arxiv.org/pdf/1706.03762.pdf), mais n'est 
    constitué que de couches ***"decoders"***.
    """
    )
    col1,col2 = st.columns([1,2])
    original1 = Image.open(image_path("Transformer_model_architecture.png"))
    original2 = Image.open(image_path("GPT2.png", ))
    col1.image(original1, use_column_width=True, caption='source: Attention is all you need')
    col2.image(original2, use_column_width=True, caption='source: J.Alammar,The Illustrated GPT-2 (Visualizing Transformer Language Models)"')

    st.markdown("""
    Les decoders étant eux mêmes constitués d'un layer "Masked Multi-head self-attention" et d'un layer "FeedForward"
    >- Le mécanisme ***"Masked self-attention"*** ne tient compte que des tokens précédents, contrairement au mécanisme classique qui tient compte également des tokens suivants
    """
    )
    original = Image.open(image_path("GPT2_masked-self-attention.png"))
    st.image(original, use_column_width=True, caption="source: J.Alammar,The Illustrated GPT-2 (Visualizing Transformer Language Models)")
    st.markdown("""
    >- En conséquence, la génération des tokens se fait token par token en fonction des tokens précedents. Le dernier token généré est ajouté aux tokens d'entrée. Le système est auto-regressif.
    """
    )
    st.markdown("""
    >- ***Word Embedding*** et ***Positionnal Encoding*** en entrée. Les matrices d'Embedding (wte) et de Positionnement (wpe) sont générés lors de l'entrainement de GPT2. Pour le modèle SMALL, la dimension de la matrice d'embedding est de 50257 (vocab_size) x 768 (embedding_size) et de 1024 (context_size) x 768 (embedding_size) pour la matrice de positional encodings.
    """
    )
    original = Image.open(image_path("GPT2_Embedding.png"))
    st.image(original, use_column_width=True, caption="source: J.Alammar,The Illustrated GPT-2 (Visualizing Transformer Language Models)")

    st.markdown("""
    >- Génération du prochain Token: L'output du premier bloc decoder est transmis au bloc suivant et ainsi de suite pour les 12 blocs du modèle SMALL. Les paramètres d'attention et de FeedForward sont spécifiques à chaque couche.
    >- Le calcul du nouveau token se fait de manière classique par multiplication du dernier output obtenu par la matrice d'embedding. L'élémement à plus forte probabilité est le token résultat.
    """
    ) 
    original = Image.open(image_path("GPT2_Output.png"))
    st.image(original, use_column_width=True, caption="source: J.Alammar,The Illustrated GPT-2 (Visualizing Transformer Language Models)")
    v_spacer(2)
    
    st.header("GPT2 Fine Tuning")
    st.markdown("""
   Comparaison des résultats obtenus par les modèles suivants :
    >- Transformer : 1 layer, 8 têtes d’attention
    >- Transformer big : 2 layers, 16 têtes d’attention
    >- GPT2-Small, pré-entraîné
    >- GPT2-Small, pré-entrainé comme précédemment et ré-entraîné sur dataset ENRON, tokenizer de 10K mots
    >- GPT2, entraîné sur dataset ENRON, tokenizer de 10K mots
    >- GPT2, entraîné sur dataset ENRON, tokenizer de 40K mots
    """
    )
    original = Image.open(image_path("GPT2_bench.png"))
    st.image(original, use_column_width=True)
    st.markdown("""
    Ci-dessus les scores obtenus par les différents modèles pour des prédictions de 1 à 5 mots.
    GPT2 avec un tokenizer à 40k mots obtient les meilleurs résultats avec 80% de lettres économisées par rapport à la saisie du texte sans dispositif d'auto-completion.
    """
    )