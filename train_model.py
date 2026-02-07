import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Load dataset
data = pd.read_csv("data/crop_data.csv")

X = data.drop("label", axis=1)
y = data["label"]

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Model
model = RandomForestClassifier(random_state=42)
model.fit(X_scaled, y)

# Ensure models folder exists
os.makedirs("models", exist_ok=True)

# Save model
joblib.dump(model, "models/crop_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("✅ Model trained and saved successfully")
