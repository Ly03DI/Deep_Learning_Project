import streamlit as st
from get_data import clean_data
import plotly.express as px
import folium
import matplotlib.pyplot as plt
from streamlit_folium import folium_static

def run_dashboard(cleaned_data, folium_map):
    # st.set_page_config(layout="wide") ## Définir la mise en page en largeur pour couvrir toute la page.

    # Définir le style CSS
    st.markdown("""
    <style>
    body {
        background-color: blue;
    }
    </style>
    """, unsafe_allow_html=True)

    
    ## Titre
    st.title("Accidentologie : base victimes")
  

    # Afficher les données sous forme de tableau
    st.write("## Tableau des données")
    st.write(cleaned_data.head(5))
    ## Ajouter des widgets
    st.sidebar.markdown("### Graphique de dispersion : Explorer la relation entre les caractéristiques :")
    x_colonnes = cleaned_data.select_dtypes(include=['object']).columns.tolist()
    y_colonnes = cleaned_data.select_dtypes(include=['int', 'float']).columns.tolist()

    x_axis = st.sidebar.selectbox("Axe des x", options=x_colonnes, index=0)
    y_axis = st.sidebar.selectbox("Axe des y", options=y_colonnes, index=1)


    st.sidebar.markdown("### Graphique à barres : Moyenne des caractéristiques par type : ")

    colonnes_x=["Mode","Catégorie","Gravité","IdUsager","Genre","Milieu","Tranche d'age"]
    colonnes_y = ["Age","Blessés Légers","Blessés hospitalisés","Tué"]

    selected_x = st.sidebar.selectbox("Sélectionner la colonne pour l'axe des x", colonnes_x)

    bar_multiselect_key = "bar_multiselect_key"
    bar_multiselect = st.sidebar.multiselect(label="Caractéristiques pour le graphique à barres", options=colonnes_y, default=["Blessés Légers"], key=bar_multiselect_key)

    ## Actions et ajustements de mise en page
    container1, container2 = st.columns(2)

    with container1:
        if x_axis and y_axis:
            scatter_fig = px.scatter(cleaned_data, x=x_axis, y=y_axis,
                                     labels={x_axis: x_axis.capitalize(), y_axis: y_axis.capitalize()},
                                     title=f"{x_axis.capitalize()} vs {y_axis.capitalize()}")
            st.plotly_chart(scatter_fig)

        if bar_multiselect and cleaned_data[selected_x].dtype == 'object':
            selected_regions = st.multiselect(label="Sélectionner les régions à comparer", options=cleaned_data['Arrondissement'].unique(), default=cleaned_data['Arrondissement'].unique())
            filtered_data = cleaned_data[cleaned_data['Arrondissement'].isin(selected_regions)]

            grouped_data = filtered_data.groupby(selected_x)[bar_multiselect].max()
            grouped_data = grouped_data.transpose()

            fig, ax = plt.subplots(figsize=(10, 6))
            grouped_data.plot(kind='bar', ax=ax)
            plt.title('Comparaison des données par Arrondissement')
            plt.xlabel(selected_x)
            plt.ylabel('Valeurs')
            plt.xticks(rotation=45, ha='right')
            plt.legend(title='Caractéristiques')
            plt.tight_layout()
            st.pyplot(fig)

        elif not bar_multiselect:
            st.sidebar.warning("Veuillez sélectionner au moins une caractéristique pour le graphique à barres.")
        elif cleaned_data[selected_x].dtype != 'object':
            st.sidebar.warning("Veuillez sélectionner une colonne catégorielle pour l'axe des x.")
        else:
            st.sidebar.warning("Les colonnes sélectionnées pour le graphique à barres ne contiennent pas de données numériques.")     

    with container2:
        with st.container():
            if x_axis and y_axis:
                # Calculer les valeurs pour le diagramme camembert à partir des données
                values = cleaned_data.groupby(x_axis)[y_axis].sum()
                # Créer le diagramme camembert avec Plotly Express
                pie_fig = px.pie(values=values, names=values.index, title=f"Répartition des valeurs par {x_axis.capitalize()}")
                st.plotly_chart(pie_fig)

        # Afficher la carte Folium
        st.write("## Carte des observations")
        folium_static(folium_map)
