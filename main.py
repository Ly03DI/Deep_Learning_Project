import streamlit as st
from get_data import load_data, clean_data
from Dashboard import run_dashboard 
from map import create_folium_map  # Assurez-vous d'importer la fonction create_folium_map depuis le fichier map.py
import folium

def main():
    # Définir la configuration de la page
    st.set_page_config(layout="wide") ## Définir la mise en page en largeur pour couvrir toute la page.

    # Charger les données à partir du fichier CSV
    file_name = "accidentologie.csv"
    data = load_data(file_name)

    # Nettoyer les données
    cleaned_data = clean_data(data)

    # Créer la carte Folium
    folium_map = create_folium_map(data)

    # Lancer le dashboard avec les données nettoyées et la carte Folium
    run_dashboard(cleaned_data, folium_map)

if __name__ == "__main__":
    main()
