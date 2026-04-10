import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load data clean
df = pd.read_csv("data/clean/traffic_clean.csv")

# Debug (opsional tapi bagus)
print("Kolom:", df.columns)

# Feature & target
X = df[['hour', 'day']]
y = df['traffic']  

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
    )

# Model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Simpan model
with open("models/traffic_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model berhasil dibuat & disimpan")