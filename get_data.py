import pandas as pd 

def load_data(nom_fichier):
    # Charger vos données depuis un fichier CSV
    data = pd.read_csv(nom_fichier, delimiter=";")
    return data

def clean_data(data):
    # Remplacer les valeurs manquantes par 0 dans les colonnes spécifiées
    # Sélectionner les colonnes de type entier
    # Remplacer les valeurs non définies par 0 dans tout le DataFrame
# Remplacer les valeurs non définies par 0 dans tout le DataFrame
    data = data.fillna(0)

    # Convertir les colonnes de type float64 en entiers
    colonnes_float = data.select_dtypes(include=['float64']).columns
    data[colonnes_float] = data[colonnes_float].astype(int)



    # data["Blessés Légers"]=  data["Blessés Légers"].fillna("0")
    # data["Blessés hospitalisés"]=  data["Blessés hospitalisés"].fillna("0")
    # data["Tué"]=  data["Tué"].fillna("0")
    # Calculer le mode de la colonne "Tranche d'age"
    mode_tranche_age = data["Tranche d'age"].mode()[0]

    # Remplacer les valeurs nulles dans la colonne "Tranche d'âge" par le mode
    data["Tranche d'age"] = data["Tranche d'age"].fillna(mode_tranche_age)
    
    data["Résumé"] = data["Résumé"].fillna("Données manquantes")
    data["Adresse"] = data["Adresse"].fillna("Adresse inconnue")

    
    # Supprimer les colonnes "arrondgeo" et "Arrondissement.1"
    data = data.drop(labels=["arrondgeo", "Arrondissement.1"], axis=1)
    
    # Convertir la colonne 'Date' en type datetime
    # data['Date'] = pd.to_datetime(data['Date'])

    # Convertir les colonnes 'Age', 'Blessés Légers', 'Blessés hospitalisés' et 'Tué' en type entier
    colonnes_entier = ['Age', 'Blessés Légers', 'Blessés hospitalisés', 'Tué']
    data[colonnes_entier] = data[colonnes_entier].astype(int)
    
    # Convertir les colonnes 'Mode', 'Catégorie', 'Gravité', 'Genre', 'Milieu', 'Tranche d'âge', 'PIM/BD PERIPHERIQUE', 'Résumé', 'Coordonnées', 'Nom arrondissement' en type str
    colonnes_categorie = ['Mode', 'Catégorie', 'Gravité', 'Genre', 'Milieu', 'Tranche d\'age', 'PIM/BD PERIPHERIQUE', 'Résumé', 'Coordonnées', 'Nom arrondissement',"Adresse"]
    data[colonnes_categorie] = data[colonnes_categorie].astype(str)
    
    return data

# file_name = "accidentologie.csv"
# data = load_data(file_name)
# data_cleaned = clean_data(data)
