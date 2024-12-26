import joblib
from sklearn.ensemble import RandomForestClassifier
import os

# Path to save the model
MODEL_PATH = "ai_models/malware_detection.pkl"

# Ensure the directory exists
os.makedirs("ai_models", exist_ok=True)

# Example Training Data (Replace this with real data)
X_train = [
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 0, 1, 0]
]

y_train = [0, 1, 1, 0]  # Example Labels (0 = Safe, 1 = Malware)

# Train a basic model
print("Training the model...")
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, MODEL_PATH)
print(f"Model saved at: {MODEL_PATH}")
