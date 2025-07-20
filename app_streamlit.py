
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load model
model = pickle.load(open('model/crop_yield_model.pkl', 'rb'))


lang = st.sidebar.selectbox("🌐 Select Language", ["English", "தமிழ்", "हिन्दी"])
labels = {
    "English": {"title": "🌾 Smart Crop Yield Predictor", "ph": "Soil pH", "rain": "Rainfall (mm)", "temp": "Temperature (°C)", "result": "Predicted Crop Yield"},
    "தமிழ்": {"title": "🌾 சாமர்த்தியமான பயிர் மகசூல் கணிப்பாளர்", "ph": "மண் pH", "rain": "மழை அளவு (மிமீ)", "temp": "வெப்பநிலை (°C)", "result": "கணிக்கப்பட்ட மகசூல்"},
    "हिन्दी": {"title": "🌾 स्मार्ट फसल उपज पूर्वानुमान", "ph": "मिट्टी का pH", "rain": "वर्षा (मिमी)", "temp": "तापमान (°C)", "result": "अनुमानित उपज"}
}
st.title(labels[lang]["title"])
soil_ph = st.sidebar.slider(labels[lang]["ph"], 4.0, 9.0, 6.5)
rainfall = st.sidebar.slider(labels[lang]["rain"], 0, 500, 200)
temperature = st.sidebar.slider(labels[lang]["temp"], 10, 45, 28)

st.title("🌾 Smart Crop Yield Predictor")
st.sidebar.header("Enter Crop Parameters")

soil_ph = st.sidebar.slider("Soil pH", 4.0, 9.0, 6.5)
rainfall = st.sidebar.slider("Rainfall (mm)", 0, 500, 200)
temperature = st.sidebar.slider("Temperature (°C)", 10, 45, 28)

if st.sidebar.button("Predict Yield"):
    features = np.array([[soil_ph, rainfall, temperature]])
    prediction = model.predict(features)[0]
    st.success(f"✅ Predicted Crop Yield: {round(prediction, 2)} quintals/ha")

# Sample dataset for visualization
df = pd.read_csv("data/yield_dataset.csv")
st.subheader("📊 Historical Yield Dataset")
st.dataframe(df.head())

st.subheader("📈 Rainfall vs Yield")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="Rainfall", y="Yield", hue="Fertilizer", ax=ax)
st.pyplot(fig)
