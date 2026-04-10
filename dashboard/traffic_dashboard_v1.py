import streamlit as st
import pickle
import pandas as pd
import os

# =========================
# LOAD MODEL
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, "models", "traffic_model.pkl")
model = pickle.load(open(model_path, "rb"))

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Traffic Prediction",
    page_icon="🚦",
    layout="centered"
)

# =========================
# HEADER
# =========================
st.markdown("<h1 style='text-align: center;'>🚦 Traffic Prediction Smart City</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Prediksi jumlah kendaraan berdasarkan waktu</p>", unsafe_allow_html=True)

st.markdown("---")

# =========================
# INPUT SECTION
# =========================
col1, col2 = st.columns(2)

with col1:
    hour = st.slider("⏰ Pilih Jam", 0, 23, 8)

with col2:
    day = st.selectbox(
        "📅 Pilih Hari",
        ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    )

day_map = {
    "Senin": 0, "Selasa": 1, "Rabu": 2,
    "Kamis": 3, "Jumat": 4, "Sabtu": 5, "Minggu": 6
}

st.markdown("---")

# =========================
# BUTTON + RESULT
# =========================
if st.button("🚀 Prediksi Sekarang"):
    input_data = pd.DataFrame([[hour, day_map[day]]], columns=['hour', 'day'])
    prediction = model.predict(input_data)[0]

    st.markdown("### 📊 Hasil Prediksi")
    
    col1, col2, col3 = st.columns(3)

    with col2:
        st.metric("🚗 Jumlah Kendaraan", int(prediction))

    # Insight sederhana
    if prediction > 120:
        st.warning("⚠️ Potensi kemacetan tinggi")
    elif prediction > 90:
        st.info("🚦 Lalu lintas sedang")
    else:
        st.success("✅ Lalu lintas lancar")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("📊 Machine Learning - Smart City | Praktikum Big Data")