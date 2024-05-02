import pandas as pd 

def load_data(nom_fichier):
    # Charger vos données depuis un fichier CSV
    data = pd.read_csv(nom_fichier, delimiter=";")
    return data

def clean_data(data):
    # Remplacer les valeurs manquantes dans la colonne "Tranche d'âge" par le mode
    mode_values = data["Tranche d'age"].mode().iloc[0]
    data["Tranche d'age"].fillna(mode_values, inplace=True)

    # Remplacer les valeurs manquantes dans les colonnes des blessures par 0 et les convertir en entier
    colonnes_a_convertir = ["Blessés Légers", "Blessés hospitalisés", "Tué"]
    data[colonnes_a_convertir] = data[colonnes_a_convertir].fillna(0).astype(int)

    # Remplacer les valeurs manquantes dans la colonne "Résumé" par "Données manquantes"
    data["Résumé"].fillna("Données manquantes", inplace=True)

    # Remplacer les valeurs manquantes dans la colonne "Adresse" par "Adresse inconnue"
    data["Adresse"].fillna("Adresse inconnue", inplace=True)

    # Supprimer les colonnes "arrondgeo" et "Arrondissement.1"
    data = data.drop(labels=["arrondgeo", "Arrondissement.1"], axis=1)

    # Convertir la colonne 'Date' en type datetime
    data['Date'] = pd.to_datetime(data['Date'])

    # Ajouter des colonnes pour le jour, le mois et l'année
    data['Jour'] = data['Date'].dt.day
    data['Mois'] = data['Date'].dt.month
    data['Année'] = data['Date'].dt.year

    # Convertir les colonnes sélectionnées en chaînes de caractères
    colonnes_categorie = ['Mode', 'Catégorie', 'Gravité', 'Genre', 'Milieu', 'PIM/BD PERIPHERIQUE', 'Résumé', 'Coordonnées', 'Nom arrondissement']
    data[colonnes_categorie] = data[colonnes_categorie].applymap(str)

    # Définir le mapping des valeurs de gravité aux nombres entiers
    mapping_gravite = {"Blessé léger": 0, "Blessé hospitalisé": 1, "Tué": 2}

    # Remplacer les valeurs de la colonne "Gravité" par les nombres entiers correspondants
    data['Gravité'] = data['Gravité'].map(mapping_gravite)

    return data
