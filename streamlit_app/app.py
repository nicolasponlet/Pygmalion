
# ######################################################################################################################
# Pygmalion
# Outil d’auto-complétion d’emails par intelligence artificielle
# Promotion		Octobre 2021 Continue DS
# DataScientest.com
#
# Participants :
# Adrien SENECAL (https://www.linkedin.com/in/adriensenecal/)
# Nicolas PONLET (https://www.linkedin.com/in/nicolasponlet/)
# Patrick HUTTER (https://www.linkedin.com/in/patrick-hutter-00668120a/)
# ######################################################################################################################

import streamlit as st
# Custom imports 
from multipage import MultiPage
from pages import GPT2, dashboard, dataset, application, analyseExploratoire, conclusion, strategie

def main():
    # Create an instance of the app 
    app = MultiPage()
    st.sidebar.title("Pygmalion")

    # Add all your applications (pages) here
    app.add_page("Le projet Pygmalion", dashboard.app)
    app.add_page("Le dataset", dataset.app)
    app.add_page("Analyse exploratoire", analyseExploratoire.app)
    app.add_page("La stratégie suivie", strategie.app)
    app.add_page("Le modèle GPT2", GPT2.app)
    app.add_page("Démo", application.app)
    app.add_page("Conclusion et perspectives", conclusion.app)

    # The main app
    app.run()

    # Group member information
    st.sidebar.info(
        "Projet DS - Promotion Octobre 2021 Continue"
        "\n\n"
        "Participants:"
        "\n\n"
        "[Adrien SENECAL](https://www.linkedin.com/in/adriensenecal/)"
        "\n\n"
        "[Nicolas PONLET](https://www.linkedin.com/in/nicolasponlet/)"
        "\n\n"
        "[Patrick HUTTER](https://www.linkedin.com/in/patrick-hutter-00668120a/)"
        "\n\n"
        "[Github](https://github.com/DataScientest-Studio/Pygmalion)"
        )
        
if __name__ == '__main__':
    main()