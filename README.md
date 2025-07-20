# 🌾 Smart Crop Yield Predictor

A real-world machine learning project that helps farmers predict crop yield based on soil pH, rainfall, and temperature. Built using Flask and Streamlit.

## 🚀 Features

- Predicts crop yield using ML (Linear Regression)
- Two interfaces: HTML frontend and Streamlit dashboard
- Rainfall vs Yield chart with fertilizer insight
- Real dataset integration
- Voice control in 3 languages (Tamil, Hindi, English) for ease of use by layman users
- Colorful frontend and responsive design
- Footer with project credits

## 🛠 Tech Stack

- Python, Flask, Streamlit
- Scikit-learn, Pandas, Numpy
- HTML, CSS, JavaScript (for web frontend)
- Seaborn & Matplotlib for visualization

## 🧪 Model

The model is trained using real agricultural data and predicts yield in quintals/hectare using Linear Regression. It considers the following features:
- Soil pH
- Rainfall (in mm)
- Temperature (in °C)

## 🗂 Project Structure

Smart_Crop_Yield_Predictor/
│
├── backend/
│ └── app.py # Flask backend for API
├── frontend/
│ ├── index.html # Web frontend
│ ├── style.css # CSS styling
│ └── script.js # JavaScript for UI interactions and voice input
├── model/
│ └── crop_yield_model.pkl # Trained ML model
├── data/
│ └── yield_dataset.csv # Agricultural dataset used for training
├── app_streamlit.py # Streamlit version for dashboard view
└── README.md # Project documentation


## 🔧 Run Instructions

### 1. Backend Flask App

```bash
cd backend
pip install flask flask-cors numpy scikit-learn
python app.py


pip install streamlit pandas matplotlib seaborn
streamlit run app_streamlit.py
'''

🧑‍💻 Developed By
Sanjay Panneerselvan
❤️ Passionate about blending AI with real-world problems.
