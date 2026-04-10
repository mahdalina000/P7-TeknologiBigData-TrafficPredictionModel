# 🚦 Smart City Traffic Prediction System
**Praktikum 7 - Teknologi Big Data**

Project ini adalah sistem prediksi volume lalu lintas berbasis Machine Learning yang dirancang untuk implementasi Smart City. Sistem ini mencakup pipeline data lengkap, mulai dari pembersihan data, pelatihan model AI, hingga visualisasi dashboard interaktif.

## 📂 Struktur Project
* `data/raw/`: Dataset lalu lintas mentah (format CSV).
* `data/clean/`: Data yang telah melalui proses pembersihan dan feature engineering.
* `scripts/`: Script Python untuk data cleaning.
* `analytics/`: Script untuk melatih model Machine Learning (Random Forest).
* `models/`: Penyimpanan model AI yang sudah dilatih (`.pkl`).
* `dashboard/`: Aplikasi dashboard interaktif berbasis Streamlit.

## 🛠️ Teknologi yang Digunakan
* **Bahasa Pemrograman:** Python 3.x
* **Library Utama:** Pandas, Scikit-Learn, Streamlit, Matplotlib.
* **Algoritma:** Random Forest Regressor.

## 🚀 Cara Menjalankan Project

1. **Pembersihan Data:**
   Jalankan script cleaning untuk merapikan data mentah.
   ```bash
   python scripts/traffic_data_cleaning_v1.py
2. Melatih Model AI:
Jalankan script modeling untuk melatih otak AI.
```bash
python analytics/traffic_ml_model_v1.py
3. Menjalankan Dashboard:
Gunakan Streamlit untuk membuka dashboard di browser.
```bash
streamlit run dashboard/traffic_dashboard_v1.py
📊 Fitur Dashboard
Visualisasi Tren: Grafik real-time volume kendaraan.
Prediksi Interaktif: Input jam, hari, dan volume sebelumnya untuk mendapatkan prediksi trafik di masa depan menggunakan model AI.
