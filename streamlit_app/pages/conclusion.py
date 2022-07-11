import streamlit as st
from utils.utils import v_spacer, image_path
from PIL import Image
import os

# @st.cache
def app():
    col1,col2 = st.columns([1,2])
    original1 = Image.open(image_path("Pygmalion_logo.jpg"))
    col1.image(original1, use_column_width=True)

    col2.title("Conclusion et perspectives")
    col2.header("...")
    v_spacer(2)

    st.markdown("### Résulats encourageants")
    st.write("En termes de résultat, ceux que nous avons obtenu sont plutôt encourageants.")

    st.markdown("#### Performances")
    image = Image.open(image_path("scores.png"))
    st.image(image)    
    st.write("En termes de résultat, ceux que nous avons obtenu sont plutôt encourageants. \
        Le niveau de performance de notre modèle à progressé de **50%** à plus de **80%**, c’est-à-dire que pour générer un texte, notre outil réduira de 80% le nombre de lettres à saisir au clavier.")   
    v_spacer(2) 

    st.markdown("#### Applications")

    st.write("Le gain de temps qui en résulte pourrait satisfaire les utilisateurs de plusieurs applications, comme l’écriture d’**emails**, de **SMS** ou autres **messageries instantanées**.")

    col1,col2,col3 = st.columns([1,2,3])
    original1 = Image.open(image_path("gmail.png"))
    col1.image(original1, width=100, use_column_width=False)
    original2 = Image.open(image_path("gmessage.png"))
    col2.image(original2, width=100, use_column_width=False)
    original3 = Image.open(image_path("messenger.png"))
    col3.image(original3, width=100, use_column_width=False)
    v_spacer(2) 

    st.write("Cet outil pourrait également être utilisé pour faciliter les **rédactions techniques** propres à chaque entreprise, comme des spécifications techniques ou fonctionnelles.")

    image = Image.open(image_path("words.png"))
    st.image(image, width=100)    
    v_spacer(2) 
    
    st.write("Il pourrait aussi être utilisé comme aide à l’écriture de programme informatique par **auto-complétion de code**.")

    image = Image.open(image_path("vscode.png"))
    st.image(image, width=100)    
    v_spacer(2) 

    st.markdown("### Limites")
    st.markdown("#### Limites techniques")
    st.write("Cependant, certains aspects peuvent être améliorés. \
        Par exemple, d’un point de vue technique, nous pourrions effectuer un apprentissage sur une **plus grande base de données**. \
        Moyennant plus de **puissance computationnelle**, nous pourrions également jouer sur les paramètres du modèle comme le nombre de **layers** ou le nombre d’**epochs**.")   
    v_spacer(2) 

    st.markdown("#### Limites fonctionnelles")
    st.write("D'un point de vue fonctionnel, le **champs lexical** du dataset est propre au milieu de l'entreprise, particulièrement celui l'**énergie**. Une diversification du champ lexical permettrait d'obtenir des réponses moins orientées.\
            \n\nDe plus, le score est basé sur la **prédiction exacte** du mot attendu. Or, le language permet d'exprimer une même idée de plusieurs façons différentes")   
    v_spacer(2) 

    st.markdown("### Perspectives")
    image = Image.open(image_path("recaptcha.png"))
    st.image(image, width=300)    
    st.write("Pour palier au fait que le score se base sur la prédiction exacte du mot attendu, l'ajout d'un ystème de validation de la **prédiction par des \"juges\"** humains, type CAPTCHA, pourrait améliorer grandement l'efficacité de notre outil.")
    v_spacer(2) 

    image = Image.open(image_path("corr_ortho.png"))
    st.image(image, width=300)    
    st.write("L'intégration d'un **correcteur orthographique** permettrait de rendre l’outil plus complet pour les utilisateurs.")
    v_spacer(2) 
