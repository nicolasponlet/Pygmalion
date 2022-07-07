import streamlit as st
from utils.utils import v_spacer, image_path
from PIL import Image

# @st.cache
def app():
    col1,col2 = st.columns([1,2])
    original1 = Image.open(image_path("Pygmalion_logo.jpg"))
    col1.image(original1, use_column_width=True)

    col2.title("Pygmalion")
    col2.header("Outil d’auto-complétion d’emails par intelligence artificielle")
    v_spacer(2)
   
    txt = "Quelques mots en introduction quant au choix du nom de ce projet : Pygmalion. Ce nom nous vient du récit d’Ovide, dans les métamorphoses, d’une légende de la mythologie grecque relatant l’histoire d’un sculpteur, Pygmalion, qui tomba amoureux de la statue qu’il a façonnée, Galatée. C’est surtout la première histoire de l’humanité qui décrit une création de l’homme qui devient vivante et dotée d’une intelligence."
    st.write(txt)
    image = Image.open(image_path("Pygmalion_priant_Venus.jpg"))
    st.image(image, caption='Jean-Baptiste Regnault (1785)', width = 666)
    txt = "Ce mythe de Pygmalion a été repris au XIXe siècle par Georges Shaw dans une pièce de théâtre qui décrit le processus d’apprentissage d’une personne sans éducation en une personne cultivée grâce à un linguiste. Pygmalion illustre, de fait, assez bien ce que nous souhaitons réaliser dans ce projet, construire un modèle capable de générer des mots à partir d’un corpus donné, mots générés en fonction du contexte."
    st.write(txt)
    st.write("https://www.theatre-classique.fr/pages/pdf/OVIDE_METAMORPHOSES_10.pdf")
    st.write("http://www.kkoworld.com/kitablar/Bernard_Shaw_Secilmis_eserler_eng.pdf")
    v_spacer(1)

    st.markdown("####  Promotion Octobre 2021 Continue")
    st.write("Data Scientist")
    st.write("https://datascientest.com/")
    v_spacer(1)

    st.write("Participants :")
    st.write("Adrien SENECAL : [Linkedin](https://www.linkedin.com/in/adriensenecal/) [Github](https://github.com/adrien-senecal)")
    st.write("Nicolas PONLET : [Linkedin](https://www.linkedin.com/in/nicolasponlet/)")
    st.write("Patrick HUTTER : [Linkedin](https://www.linkedin.com/in/patrick-hutter-00668120a/)")
    v_spacer(2)

    st.write("Le repo github complet : https://github.com/DataScientest-Studio/Pygmalion")
 