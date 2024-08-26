import streamlit as st
import pickle
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
st.title("Diabetes Prediction App")
