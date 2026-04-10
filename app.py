import streamlit as st
import joblib

model = joblib.load("model.pkl")

st.title("Water Prediction")

temp = st.number_input("Temperature")
rain = st.number_input("Rainfall")
humidity = st.number_input("Humidity")

if st.button("Predict"):
    result = model.predict([[temp, rain, humidity]])
    st.success(result)
