import streamlit as st
from utils.utils import v_spacer, image_path
from PIL import Image
import os

# @st.cache
def app():
    col1,col2 = st.columns([1,2])
    original1 = Image.open(image_path("Pygmalion_logo.jpg"))
    col1.image(original1, use_column_width=True)

    col2.title("Le dataset ENRON")
    col2.header("Les e-mails de la société ENRON")
    v_spacer(2)

    st.markdown("#### Illustration de l'auto-complétion")

    image = Image.open(image_path("dataset.png"))
    st.image(image)
    v_spacer(2) 
    
    st.markdown("#### Choix du jeu de données")
    st.write("Nous avons démarré ce projet par l’étude de **différents datasets** pour générer notre corpus. \
        \n- Les e-mails d'**Hillary Clinton** lors de sa mission de Secrétaire d’Etat en 2015  \
        \n- Les e-mails de la société **ENRON**  \
        \n\nLe dataset retenu a été finalement celui de la société **ENRON**, plus riche en contenu et plus proche du monde industriel. \
        \n\nCependant il est intéressant de noter qu’à tout moment il serait possible de remplacer le dataset par un autre. Nous pourrions, par la suite, **comparer la performance** de notre modèle avec un autre dataset pour mesurer sa robustesse.")
    v_spacer(2)

    st.markdown("#### Principales caractéristiques du jeu de données ENRON")
    st.write("- Environ **500 000 mails** échangés entre **158 collaborateurs** du groupe \
        \n- Libre d’accès et de droit, suite à la faillite du groupe en 2001. \
        \n- Répond à une **problématique d’entreprise** appartenant à un domaine d’activité bien précis qu'est l'**énergie**. \
        \n- https://www.cs.cmu.edu/~./enron/ :")
    v_spacer(2)
        
    st.markdown("#### Pré-traitement des données")
    st.write("Le pré-traitement a consisté à : \
        \n- Transformation des caractères majuscules en minuscules \
        \n- Insertion d’une espace devant les caractères ?!, ¿ \
        \n- Remplacement des caractères différents de A-Z,a-z,0-9,., ?, !,, par une espace \
        \n- Suppression des espaces multiples par une seule \
        \n- Remplacement des formes de verbes contractés par leur forme complète (par ex. won’t en will not) \
        \n- Élimination de tout ce qui précède  le mot «Subject: », afin de supprimer le contenu qui précède une réponse ou un transfert. \
        \n- Découpage de chaque email en phrase (chaîne de caractère se terminant par “.”, “!”, “?”) pour que le dataset soit constitué d’une phrase par ligne.")    
    
    st.write("Après nettoyage des données, nous obtenons un corpus avec : \
        \n- **497 560** mails \
        \n- **135 millions** de mots \
        \n- **303 752** mots distincts après nettoyage")
    v_spacer(2) 
    
    st.markdown("#### Thématiques fréquentes")
    image = Image.open(image_path("Top_20_sujets_emails.png"))
    st.image(image, caption='Top 20 des sujets des emails')

    st.write("On y retrouve les centres d'intérêts classiques d'un grand groupe industriel : \
        \n- **Communication** : Enron mentions, EnTouche Newsletter, William Energy New Live \
        \n- **Organisation du groupe** : Organization(al) Announcement \
        \n- **Résultats et évaluation des bonus** : Mid-year perf feedback, year end Perf. feedback \
        \n- **Indicateurs** : energy issues, power indices, gas indices \
        \n- Plus spécifique à Enron, le mail à Ken Lay (CEO d'Enron) envoyé par plus de 1124 employés suite à la faillite du groupe, demandant le versement des profits réalisés par Ken Lay lors de la vente d'actions d'Enron juste avant que la faillite du groupe Enron ne soit rendue publique. \
        \n- Enfin le suivi automatique de congestion du réseau électrique en Californie appelé HourAhead.(Schedule crawler: HourAhead Failure)")
    v_spacer(2)
    
    st.markdown("#### Fréquence des mots")
    image = Image.open(image_path("Frequence_des_mots_sujets.png"))
    st.image(image, caption='Top 15 des mots les plus fréquents dans les sujets des mails')

    st.write("La liste des mots les plus fréquents permet également de synthétiser les axes prioritaires de l'activité des employés d'Enron. \
        \n- En première place on retrouve logiquement le nom de la société **Enron** \
        \n- En deuxième, le mal des grandes sociétés : les **réunions**. \
        \n- Les mots suivants décrivent bien l'activité du groupe (**energy**, **gas**) et le système de pilotage en énergie de la Californie (HourAhead + codesite)")

    