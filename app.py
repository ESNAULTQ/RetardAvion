import streamlit as st
import joblib
import pandas as pd

# Charger le modèle sauvegardé
model = joblib.load('logistic_regression_model.joblib')

carrier_mapping = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'}



# Titre de l'application
st.title('Prédictions de Retard des Vols')

# Instructions
st.write("Veuillez entrer les caractéristiques du vol pour prédire le retard.")

# Créer des champs d'entrée pour les caractéristiques du vol
# Assurez-vous que les champs d'entrée correspondent aux caractéristiques attendues par le modèle
MONTH = st.selectbox("Mois de départ", list(carrier_mapping))
CRS_DEP_TIME = st.number_input('Heure de départ (HHMM)')
# Ajouter des champs pour toutes les autres caractéristiques nécessaires
# Par exemple, si vous avez 10 caractéristiques
CRS_ARR_TIME = st.number_input("Heure d'arrivé (HHMM)")
DISTANCE = st.number_input('Distance (KM)') 


# Créer un dataframe avec les valeurs d'entrée
input_data = pd.DataFrame({
    'MONTH': [MONTH],
    'CRS_DEP_TIME': [CRS_DEP_TIME],
    'CRS_ARR_TIME': [CRS_ARR_TIME],
    'DISTANCE': [DISTANCE],

    
})

# Faire une prédiction avec le modèle chargé
if st.button('Prédire'):
    prediction = model.predict(input_data)
    st.write(f'La prédiction de retard est : {prediction[0]}')

# Pour exécuter cette application Streamlit, utilisez la commande suivante dans votre terminal :
# streamlit run app.py
