
import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd

def create_folium_map(data):
    observations_par_arrondissement = data.groupby('Nom arrondissement').size()
    carte = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

    for arrondissement, observations in observations_par_arrondissement.items():
        arrondissement_data = data[data['Nom arrondissement'] == arrondissement]
        total_observations = len(arrondissement_data)
        popup_content = f"<div style='max-height: 300px; overflow-y: auto;'><b>Arrondissement {arrondissement}</b><br>"
        popup_content += f"Nombre total d'observations : {total_observations}<br>"
        for column in arrondissement_data.columns:
            if column != 'Nom arrondissement':
                popup_content += f"{column} : {arrondissement_data[column].iloc[0]}<br>"
        popup_content += "</div>"
        folium.CircleMarker(
            location=[arrondissement_data['Latitude'].mean(), arrondissement_data['Longitude'].mean()],
            radius=observations/100,
            popup=folium.Popup(popup_content, max_width=300, max_height=300),
            color='blue',
            fill=True,
            fill_color='blue'
        ).add_to(carte)
    return carte

