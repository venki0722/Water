import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🌾 Crop Prediction App")

# Inputs from user
temp = st.number_input("Temperature")
rainfall = st.number_input("Rainfall")
humidity = st.number_input("Humidity")

# Predict button
if st.button("Predict"):
    input_data = np.array([[temp, rainfall, humidity]])
    prediction = model.predict(input_data)

    st.success(f"Prediction: {prediction[0]}")
    import joblib
model = joblib.load("model.pkl")
