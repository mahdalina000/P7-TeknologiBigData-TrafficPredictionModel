import pandas as pd

df = pd.read_csv("data/raw/traffic_smartcity_v1.csv")

print(df.head())

df.dropna(inplace=True)

df['datetime'] = pd.to_datetime(df['datetime'])

df['hour'] = df['datetime'].dt.hour
df['day'] = df['datetime'].dt.dayofweek

df.to_csv("data/clean/traffic_clean.csv", index=False)

print("✅ Data cleaning selesai")