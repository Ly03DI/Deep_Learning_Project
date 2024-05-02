# import joblib
# import pandas as pd
# import streamlit as st
# import plotly.express as px
# from get_data import load_data, clean_data
# # Charger le modèle et le préprocesseur à partir des fichiers sauvegardés
# trained_model = joblib.load('trained_model.pkl')
# preprocessor = joblib.load('preprocessor.pkl')
# data = load_data("accidentologie.csv")
# cleaned_data = clean_data(data)

# # Ajouter une section pour la prédiction et la visualisation
# st.title("Prédiction de la gravité de l'accident et visualisation")

# # Demander à l'utilisateur de fournir les valeurs des caractéristiques
# jour_utilisateur = st.number_input("Jour de l'accident", min_value=1, max_value=31, step=1)
# mois_utilisateur = st.number_input("Mois de l'accident", min_value=1, max_value=12, step=1)
# annee_utilisateur = st.number_input("Année de l'accident", min_value=1900, max_value=2100, step=1)
# arrondissement_utilisateur = st.text_input("Arrondissement de l'accident")
# mode_utilisateur = st.text_input("Mode ")
# categorie_utilisateur = st.text_input("Catégorie de l'accident")
# age_utilisateur = st.number_input("Âge de la personne impliquée", min_value=1, max_value=150, step=1)
# genre_utilisateur = st.selectbox("Genre de la personne impliquée", ["Homme", "Femme"])

# # Créer un DataFrame pandas à partir des données utilisateur
# user_input = pd.DataFrame({
#     "Jour": [jour_utilisateur],
#     "Mois": [mois_utilisateur],
#     "Année": [annee_utilisateur],
#     "Arrondissement": [arrondissement_utilisateur],
#     "Mode": [mode_utilisateur],
#     "Catégorie": [categorie_utilisateur],
#     "Age": [age_utilisateur],
#     "Genre": [genre_utilisateur]
# })

# # Prétraiter les données utilisateur avec le préprocesseur
# user_input_processed = preprocessor.transform(user_input)

# # Faire la prédiction en utilisant le modèle entraîné
# predicted_gravity_probs = trained_model.predict(user_input_processed)

# # Sélectionner la classe avec la probabilité la plus élevée
# predicted_gravity_class = predicted_gravity_probs.argmax(axis=1)

# # Afficher la prédiction de gravité de l'accident
# classes = ["léger", "grave", "hospitalisation"]
# predicted_gravity_label = classes[predicted_gravity_class[0]]
# st.write("Gravité de l'accident prédite :", predicted_gravity_label)

# # # Ajouter un graphique à l'autre côté du tableau de bord
# # st.write("## Visualisation des données")

# # # Par exemple, vous pouvez afficher un graphique à barres pour montrer la distribution des catégories d'accidents
# # bar_data = cleaned_data['Catégorie'].value_counts()
# # bar_fig = px.bar(bar_data, x=bar_data.index, y=bar_data.values, labels={'x':'Catégorie', 'y':'Nombre d\'accidents'})
# # st.plotly_chart(bar_fig)

import joblib
import pandas as pd
import streamlit as st
import plotly.express as px
from get_data import load_data, clean_data

# Charger le modèle et le préprocesseur à partir des fichiers sauvegardés
trained_model = joblib.load('trained_model.pkl')
preprocessor = joblib.load('preprocessor.pkl')
data = load_data("accidentologie.csv")
cleaned_data = clean_data(data)

# Ajouter une section pour la prédiction et la visualisation
st.title("Prédiction de la gravité de l'accident")

# Demander à l'utilisateur de fournir les valeurs des caractéristiques
jour_utilisateur = st.number_input("Jour de l'accident", min_value=1, max_value=31, step=1)
mois_utilisateur = st.number_input("Mois de l'accident", min_value=1, max_value=12, step=1)
annee_utilisateur = st.number_input("Année de l'accident", min_value=1900, max_value=2100, step=1)
arrondissement_utilisateur = st.text_input("Arrondissement de l'accident")
mode_utilisateur = st.text_input("Mode ")
categorie_utilisateur = st.text_input("Catégorie de l'accident")
age_utilisateur = st.number_input("Âge de la personne impliquée", min_value=1, max_value=150, step=1)
genre_utilisateur = st.selectbox("Genre de la personne impliquée", ["Masculin", "Feminin"])

# Vérifier si l'utilisateur a fourni des données
if (jour_utilisateur is not None) and (mois_utilisateur is not None) and (annee_utilisateur is not None) and \
        (arrondissement_utilisateur != "") and (mode_utilisateur != "") and (categorie_utilisateur != "") and \
        (age_utilisateur is not None) and (genre_utilisateur != ""):
    
    # Créer un DataFrame pandas à partir des données utilisateur
    user_input = pd.DataFrame({
        "Jour": [jour_utilisateur],
        "Mois": [mois_utilisateur],
        "Année": [annee_utilisateur],
        "Arrondissement": [arrondissement_utilisateur],
        "Mode": [mode_utilisateur],
        "Catégorie": [categorie_utilisateur],
        "Age": [age_utilisateur],
        "Genre": [genre_utilisateur]
    })

    # Prétraiter les données utilisateur avec le préprocesseur
    user_input_processed = preprocessor.transform(user_input)

    # Faire la prédiction en utilisant le modèle entraîné
    predicted_gravity_probs = trained_model.predict(user_input_processed)

    # Sélectionner la classe avec la probabilité la plus élevée
    predicted_gravity_class = predicted_gravity_probs.argmax(axis=1)

    # Afficher la prédiction de gravité de l'accident
    classes = ["léger", "grave", "hospitalisation"]
    predicted_gravity_label = classes[predicted_gravity_class[0]]
    st.write("Gravité de l'accident prédite :", predicted_gravity_label)
