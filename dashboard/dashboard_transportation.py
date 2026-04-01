import streamlit as st
import pandas as pd
import os
import time
import plotly.express as px
from datetime import datetime

# Konfigurasi Halaman Dasar
st.set_page_config(page_title="Smart Transportation Dashboard", layout="wide")

DATA_PATH = "data/serving/transportation"

# Fungsi Loading Data (Memastikan data terbaru yang diambil)
def load_data():
    if not os.path.exists(DATA_PATH):
        return pd.DataFrame()
    files = [f for f in os.listdir(DATA_PATH) if f.endswith(".parquet")]
    df_list = []
    for f in files:
        f_path = os.path.join(DATA_PATH, f)
        try:
            if os.path.getsize(f_path) > 0:
                df_list.append(pd.read_parquet(f_path))
        except:
            continue
    return pd.concat(df_list, ignore_index=True) if df_list else pd.DataFrame()

# Loop Utama
placeholder = st.empty()

while True:
    with placeholder.container():
        df = load_data()

        if df.empty:
            st.info("🔄 Menunggu data dari Spark Streaming...")
            time.sleep(3)
            continue

        # 1. JUDUL (Header sesuai modul)
        st.title("🚦 Smart Transportation Real-Time Analytics")
        st.write(f"Terakhir diperbarui: {datetime.now().strftime('%H:%M:%S')}")

        # 2. METRIK (4 Metrik Utama seperti di foto modul)
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Trips", f"{len(df):,}")
        m2.metric("Total Revenue", f"Rp {int(df['fare'].sum()):,}")
        m3.metric("Avg Distance", f"{df['distance'].mean():.2f} km")
        m4.metric("Avg Fare", f"Rp {int(df['fare'].mean()):,}")

        st.markdown("---")

        # 3. GRAFIK (Susunan sampingan seperti di modul)
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Revenue per Location")
            # Agregasi data untuk grafik batang
            loc_rev = df.groupby("location")["fare"].sum().reset_index()
            fig1 = px.bar(loc_rev, x="location", y="fare", color="location")
            # Key unik untuk menghindari Duplicate ID Error di tahun 2026
            st.plotly_chart(fig1, width='stretch', key=f"bar_{int(time.time())}")

        with col2:
            st.subheader("Vehicle Distribution")
            # Agregasi data untuk grafik pie
            veh_dist = df.groupby("vehicle_type")["trip_id"].count().reset_index()
            fig2 = px.pie(veh_dist, values="trip_id", names="vehicle_type")
            st.plotly_chart(fig2, width='stretch', key=f"pie_{int(time.time())}")

        # 4. TABEL DATA (Bagian bawah sesuai modul)
        st.subheader("Live Trip Data")
        # Menampilkan 10 data terbaru
        st.dataframe(df.sort_values("timestamp", ascending=False).head(10), width='stretch')

    # Delay refresh sesuai simulasi streaming
    time.sleep(3)
