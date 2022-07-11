
import streamlit as st
from utils.utils import v_spacer, image_path
from PIL import Image

# @st.cache
def app():
    col1,col2 = st.columns([1,2])
    original1 = Image.open(image_path("Pygmalion_logo.jpg"))
    col1.markdown("")
    col1.image(original1, use_column_width=True)

    col2.title("La stratégie suivie")
    col2.header("Construire un système d'autocomplétion")
    v_spacer(2) 
    st.header("0. La problématique")
    st.markdown("""
    Comment à partir de notre dataset composé de ***497 560 e-mails*** comprenants ***135 millions de mots***, être en mesure de proposer la lettre suivante d'une séquence en cours de saisie?
    """
    )
   
    original = Image.open(image_path("process2.png"))
    st.image(original, use_column_width=True)

    
    v_spacer(2)

    st.header("1. Comment mesurer la performance de notre modèle?")
    st.markdown("""
    Prérequis à cette étude, la définition d'une métrique permettant de quantifier la performance de nos différents modèles.\n
    La métrique retenue est l'économie de lettres saisies grâce à l'autocompletion.
    """
    )
    original = Image.open(image_path("score.png"))
    st.image(original,use_column_width=True)

    st.header("2. Calcul simple de probabilité")
    col1,col2 = st.columns([1,2])
    original1 = Image.open(image_path("jauge1.png"))
    col1.image(original1, use_column_width=True)
    col2.markdown("""
    Déterminer la lettre la plus probable connaissant les lettres précédentes. Le résultat est plutôt bon, considérant la simplissité du modèle. 49% sera notre benchmark. Premier axe d'amélioration, la prise en compte des mots précédents.
    """
    )

    st.header("3. Prise en compte du contexte à l'aide de n_grammes")
    col1,col2 = st.columns([1,2])
    original1 = Image.open(image_path("jauge2.png"))
    col1.image(original1, use_column_width=True)
    col2.markdown("""
    L'amélioration du résultat obtenu est intéressante. Nous passons d'un score de 49% à 59% grâce à la prise en compte des 2 mots précedents. 
    Par contre les temps de calculs sont extrêmement longs, déjà pour les bi-grammes et encores plus longs pour pour les n-grammes d'ordres plus élevés. 
    Pour réduire les temps de calculs des filtres ont étés mis en place afin de réduire la taille du dataset, mais malgré cet artifice les temps de taritements nous font abandonner cette option.
    """
    )

    st.header("3. Prise en compte du contexte à l'aide des Bags of Words (CBOW)")
    st.markdown("""
    La technique du "word embedding" utilisée dans les BOW nous permet de mesurer la proximité entre les mots de notre corpus. 
    L'intérêt de cette solution est de déterminer le "mot suivant" le plus probable et donc les lettres le composant.
    Nous avons explorés différents modèles soit pré-entrainés, soit entrainés sur notre dataset sur une base de 10000  et 50000 emails.
    L'objet de cette étude est de déterminer la bonne taille de dataset pour la poursuite de l'étude.
    Pas de calcul de score dans cette étude, nous avons utilisé une métrique standard "l'accuracy" sur les données d'entrainement et de validation.
    """
    )
    col1,col2 = st.columns([1,1])
    original1 = Image.open(image_path("CBOW2.png"))
    col1.image(original1, use_column_width=True)
    original2 = Image.open(image_path("CBOW3.png"))
    col2.image(original2, use_column_width=True)

    st.header("4. RNN avec mécanisme d'attention")
    original1 = Image.open(image_path("seq2seq_Attn.png"))
    
    st.markdown("""
    Nous avons complété le modèle BOW en ajoutant le mécanisme d'attention en mesure de pondérer l'importance des mots dans une séquence.
    Deux modèles ont été comparés sur base des mécanismes de Bahdanau et de Luong. 
    Nous avons obtenu des pédictions de "mot suivant" exactes dans 72% des cas avec le modèle Bahdanau. 
    """
    )
    st.image(original1, use_column_width=True)

    st.header("5. Transformer")
    col1,col2 = st.columns([1,2])
    original1 = Image.open(image_path("jauge3.png"))
    
    col1.markdown("""
    Evolution du modèle Seq2Seq, le transformer ne s'appuie que sur le mécanisme d'attention.
    Nous avons construit deux modèles 
    >- 8 têtes d'attention / 1 layer
    >- 16 têtes d'attention / 2 layers
    Nous n'avons pas mesuré un impac significatif sur la performance.
    Le score obtenu est de 61%, meilleur score pour le momment
    \n
    """
    )
    col1.image(original1, use_column_width=True)
    original3 = Image.open(image_path("Transformer_model_architecture.png"))
    col2.image(original3, use_column_width=True)

    
    st.header("6. GPT2")
    col1,col2 = st.columns([1,2])
    original1 = Image.open(image_path("jauge4.png"))
    col1.image(original1, use_column_width=True)
    col2.markdown("""
    Enfin le transformer GPT2, qui intègre un modèle de language. Nous testons la version SMALL, soit en version pré-entrainée, soit entrainée sur notre dataset.
    Nous atteignons ici un score de 80% avec la dernière configuration.
    """
    )