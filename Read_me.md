# Projet de Dashboard d'Analyse de Données

Ce projet vise à créer un tableau de bord interactif pour l'analyse "Accidentologie : base victimes"
<p>Données issues de l’application nationale TRAxy (système d’information de l’observatoire national interministériel à la sécurité routière (ONISR))

Pour chaque accident corporel (soit un accident survenu sur une voie ouverte à la circulation publique, impliquant au moins un véhicule et ayant fait au moins une victime ayant nécessité des soins), des saisies d’information décrivant l’accident sont effectuées par l’unité des forces de l’ordre (police, gendarmerie, etc.) qui est intervenue sur le lieu de l’accident. Ces saisies sont rassemblées dans une fiche intitulée bulletin d’analyse des accidents corporels. L’ensemble de ces fiches constitue le fichier national des accidents corporels de la circulation dit « Fichier BAAC » administré par l’Observatoire national interministériel de la sécurité routière "ONISR".
Parmi les victimes, on distingue :
les personnes tuées : personnes qui décèdent du fait de l’accident, sur le coup ou dans les trente jours qui suivent l’accident,
les personnes blessées : victimes non tuées.
Parmi les personnes blessées, il convient de différencier :
les blessés dits « hospitalisés » : victimes hospitalisées plus de 24 heures,
les blessés légers : victimes ayant fait l'objet de soins médicaux mais n'ayant pas été admises comme patients à l'hôpital plus de 24 heures </p>

## Guide de l'Utilisateur

Pour déployer et utiliser le tableau de bord sur une autre machine, suivez les étapes suivantes :

1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/votre_utilisateur/nom_depot.git
2. Assurez-vous d'avoir Python et pip installés sur votre machine.
3. Installez les dépendances requises à l'aide de pip :
                 "pip install -r requirements.txt"
4. Lancez le tableau de bord en exécutant le fichier main.py :
5. Accédez au tableau de bord dans votre navigateur en ouvrant l'URL indiquée dans la console.
    ou (lancez Streamlit run main.py)

## Rapport d'Analyse
Le rapport d'analyse met en évidence les principales conclusions tirées des données. Voici quelques points saillants :

Analyse de la relation entre différentes caractéristiques à l'aide de graphiques de dispersion et de graphiques à barres.
Répartition des valeurs par catégorie à l'aide de diagrammes camembert.
Visualisation des observations sur une carte interactive pour une meilleure compréhension spatiale.

Répartition des victimes par type d'accident : la répartition des victimes entre les personnes tuées et les personnes blessées.
Gravité des blessures : Une analyse approfondie pourrait être effectuée pour examiner la gravité des blessures chez les personnes blessées, en distinguant les blessures légères des blessures nécessitant une hospitalisation. Cela permettrait de comprendre la proportion de blessures graves par rapport à l'ensemble des blessures.
Concentration géographique : Une analyse géographique pourrait mettre en évidence les zones où les accidents corporels sont les plus fréquents, ce qui pourrait contribuer à orienter les efforts de prévention et de sécurité routière.


### df_cleaned.head(5)
![Texte alternatif](./data/tabel.png)
## Guide du Développeur
get_data.py : Ce fichier contient une fonction load_data pour charger les données à partir de la source et une autre fonction clean_data qui sert à nettoyer et transformer les données si nécessaire. Cela permet d'avoir un module dédié à la manipulation des données, ce qui rend le code plus modulaire et facile à gérer.
dashboard.py : Ce fichier est responsable de la création du tableau de bord interactif à l'aide d'une bibliothèque comme Streamlit. Vous pouvez décrire les différentes parties du tableau de bord, les widgets utilisés pour l'interaction avec les données, et comment les visualisations sont générées à partir des données chargées.
main.py : Ce fichier est le point d'entrée de l'application. Il importe les fonctions et les classes nécessaires des autres fichiers, et il les utilise pour exécuter l'application. Il peut également contenir des configurations de base pour l'exécution de l'application, telles que la configuration de la mise en page ou des paramètres spécifiques.

Dépendances requises pour le développement :

- Streamlit : Une bibliothèque Python pour la création d'applications web interactives avec des données.
- Pandas : Une bibliothèque Python pour la manipulation et l'analyse des données.
- Plotly : Une bibliothèque Python pour la création de graphiques interactifs.
- Folium : Une bibliothèque Python pour la création de cartes interactives.
- Matplotlib : Une bibliothèque Python pour la création de graphiques statiques.
- streamlit_folium : Une extension pour Streamlit permettant d'intégrer des cartes Folium dans les applications Streamlit.

