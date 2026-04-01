import pandas as pd

def calculate_metrics(df):
    """
    Fungsi untuk menghitung statistik utama dari data transportasi.
    Dataframe (df) berasal dari file parquet yang dibaca di dashboard.
    """
    
    # Jika data masih kosong, kembalikan nilai default agar dashboard tidak error
    if df is None or df.empty:
        return {
            "total_trips": 0,
            "avg_fare": 0.0,
            "avg_distance": 0.0,
            "total_revenue": 0,
            "top_location": "N/A"
        }
    
    # 1. Menghitung Total Perjalanan
    total_trips = len(df)
    
    # 2. Menghitung Rata-rata Tarif (Fare)
    avg_fare = df['fare'].mean()
    
    # 3. Menghitung Rata-rata Jarak (Distance)
    avg_distance = df['distance'].mean()
    
    # 4. Menghitung Total Pendapatan (Revenue)
    total_revenue = df['fare'].sum()
    
    # 5. Mencari Lokasi Paling Populer (Modus)
    if 'location' in df.columns and not df['location'].empty:
        top_location = df['location'].mode()[0]
    else:
        top_location = "N/A"

    # Mengembalikan hasil dalam bentuk Dictionary
    return {
        "total_trips": total_trips,
        "avg_fare": avg_fare,
        "avg_distance": avg_distance,
        "total_revenue": total_revenue,
        "top_location": top_location
    }

def get_daily_trend(df):
    """
    (Opsional) Fungsi tambahan untuk melihat tren per jam jika dibutuhkan dashboard
    """
    if df.empty or 'timestamp' not in df.columns:
        return pd.DataFrame()
        
    df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
    trend = df.groupby('hour').size().reset_index(name='count')
    return trend
