from get_data import load_data, clean_data
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import joblib
from imblearn.under_sampling import RandomUnderSampler

# Fonction pour rééquilibrer les classes par sous-échantillonnage
def balance_classes(X_train, y_train):
    # Utiliser RandomUnderSampler pour sous-échantillonner les classes majoritaires
    rus = RandomUnderSampler(random_state=42)
    X_train_balanced, y_train_balanced = rus.fit_resample(X_train, y_train)
    return X_train_balanced, y_train_balanced

# Fonction pour créer et entraîner le modèle
def build_train_model(X_train, y_train, X_test, y_test, epochs=10, batch_size=32, validation_split=0.2):
    # Construction du préprocesseur
    categorical_cols = ['Arrondissement', 'Mode', 'Catégorie', 'Genre']
    numeric_cols = ['Jour', 'Mois', 'Année', 'Age']

    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', categorical_transformer, categorical_cols),
            ('num', numeric_transformer, numeric_cols)
        ]
    )

    # Prétraiter les données
    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)

    # Construction du modèle
    model = Sequential([
        Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        Dropout(0.5),
        Dense(64, activation='relu'),
        Dropout(0.5),
        Dense(3, activation='softmax')
    ])

    # Compilation du modèle
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Entraînement du modèle
    history = model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=validation_split, verbose=0)

    # Évaluation du modèle
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Loss: {loss}, Accuracy: {accuracy}')

    return model, preprocessor

# Charger les données
data = load_data("accidentologie.csv")
cleaned_data = clean_data(data)

# Sélectionner les caractéristiques pertinentes
features = ["Jour", "Mois", "Année", "Arrondissement", "Mode", "Catégorie", "Age", "Genre"]
X = cleaned_data[features]
y = cleaned_data["Gravité"]

# Séparation des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Rééquilibrer les classes
X_train_balanced, y_train_balanced = balance_classes(X_train, y_train)

# Construire et entraîner le modèle
trained_model, preprocessor = build_train_model(X_train_balanced, y_train_balanced, X_test, y_test)

# Sauvegarder le modèle et le préprocesseur
joblib.dump(trained_model, 'trained_model.pkl')
joblib.dump(preprocessor, 'preprocessor.pkl')
