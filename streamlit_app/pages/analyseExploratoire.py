import streamlit as st
from utils.utils import v_spacer, image_path
from PIL import Image
import os

# @st.cache
def app():
    col1,col2 = st.columns([1,2])
    original1 = Image.open(image_path("Pygmalion_logo.jpg"))
    col1.image(original1, use_column_width=True)

    col2.title("Analyse exploratoire")
    col2.header("Les e-mails de la société ENRON")
    v_spacer(2)

    st.write("Une première analyse du dataset ENRON nous donne les volumétries suivantes : \
        \n- **497 560** mails \
        \n- **135 millions** de mots \
        \n- **303 752** mots distincts après nettoyage")
    v_spacer(2) 

    st.markdown("### Pré-traitement des données")

    st.write("Le pré-traitement a consisté à : \
        \n- Transformation des caractères majuscules en minuscules \
        \n- Insertion d’une espace devant les caractères ?!, ¿ \
        \n- Remplacement des caractères différents de A-Z,a-z,0-9,., ?, !,, par une espace \
        \n- Suppression des espaces multiples par une seule \
        \n- Remplacement des formes de verbes contractés par leur forme complète (par ex. won’t en will not) \
        \n- Élimination de tout ce qui précède  le mot «Subject: », afin de supprimer le contenu qui précède une réponse ou un transfert. \
        \n- Découpage de chaque email en phrase (chaîne de caractère se terminant par “.”, “!”, “?”) pour que le dataset soit constitué d’une phrase par ligne.")
    image = Image.open(image_path("dataset.png"))
    st.image(image, caption='Dataset')

    v_spacer(2) 

    st.markdown("### Occurence des mots")
    st.markdown("#### Distribution des mots les plus fréquents et word cloud")
    image = Image.open(image_path("Frequence_+_WC.png"))
    st.image(image, caption='Wordcloud')
    st.write("**Avec stop words** :  \
        \n- **Peu de mots** se retrouvent **très représentés**, puis les occurrences diminuent progressivement \
        \n- Ces derniers occupent très largement les 1ères places des mots les plus représentés")
    st.write("**Sans stop words** :  \
        \n- Différence d'un **facteur 10** en terme d'occurence pour le mot le plus fréquent avec et sans stop words \
        \n- ENRON en tête, puis décroissance progressive")
    v_spacer(2) 

    st.markdown("#### Faut-il conserver les stop words ?")
    st.write("Le choix de conserver ou non les stop words dépend de la problématique.")
    st.write("Pour une analyse de **sens** ou de **sentiments**, les stop words ne portent pas d'informations pertinentes. \
        \n En revanche, ils alourdissent le modèle qui doit en tenir compte dans sa couche d'embedding.")
    st.write("Pour une probématique de **traduction** ou d'**auto-complétion**, tous les mots comptent et doivent être exploités. Le choix de conserver les stop words est donc évident.")
    v_spacer(2) 

    st.markdown("### Occurence des lettres")
    st.markdown("#### Matrice de corrélation")
    image = Image.open(image_path("Probabilité_d'obtenir_chaque_lettre.png"))
    st.image(image, caption='Matrice de corrélation des lettres')    
    st.write("La figure ci-dessus montre sous forme de **hitmap** la probabilité de chaque lettre de l'alphabet de suivre une lettre donnée et ce, pour toute les lettres.")
    st.write("**Observations notables** : \
        \n- La lettre **Q** est presque systématiquement suivie de la lettre **U** \
        \n- Les lettres **V** et **Z** sont souvent suivies de la lettre **E** \
        \n- La lettre **Y** se trouve très souvent en fin de mot")
    v_spacer(2) 

    st.markdown("#### Utilisation du type")
    image = Image.open(image_path("Type_de_lettre_suivante.png"))
    st.image(image, caption='Type de la lettre suivante en fonction de la lettre en cours', width=666)
    st.write("- Lorsque la lettre en cours est une **voyelle**, la lettre suivante est une consonne dans **75%** des cas \
            \n- Lorsque la lettre en cours est une **consonne**, la lettre suivante est majoritairement une voyelle, mais dans une moindre mesure que précédemment. Les consonnes sont donc davantage doublées (identiques ou non) que les voyelles \
            \n- Les consonnes terminent davantage les mots que les voyelles")
    v_spacer(2) 

    st.markdown("### Ce que nous apporte l'occurence des lettres ou des mots")
    st.write("L'occurence des lettres ou des mots peut permettre un gain significatif de performance dans la prédiction de la lettre suivante, comparé à une suggestion aléatoire.")
    st.write("Par exemple : \
        \n- Si l'utilisateur tape un **Q**, il est quasiment certain que l'outil ait juste en proposant un **U** \
        \n- Si l'utilisateur tape une voyelle, cette dernière sera suivie par une consonne dans **75%** des cas. Proposer une consonne réduit donc les suggestions possibles comparé au hasard. \
        \n Cependant, le gain en efficacité est margial. Il va donc falloir employer des modèles plus performants.")
    v_spacer(2) 

