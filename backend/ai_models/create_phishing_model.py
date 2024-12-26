import tensorflow as tf
import numpy as np

# Define a simple neural network model
model = tf.keras.Sequential([
    # Input layer expecting 3 
    # #- features: len(url), count("."), count("-")
    tf.keras.layers.Dense(64, activation='relu', input_shape=(3,)),  
    # Output layer: Sigmoid activation for binary classification (safe or malicious)
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Generate some random data to simulate training
# You can ignore this part, as we are only interested in creating the model
X_train = np.random.rand(100, 3)  # Random features (100 samples with 3 features)
y_train = np.random.randint(0, 2, 100)  # Random labels (0 or 1)

# Train the model on the random data (optional for the placeholder, can be skipped)
model.fit(X_train, y_train, epochs=1)

# Save the model as 'phishing_detector.h5'
model.save('ai_models/phishing_detector.h5')

print("Placeholder model saved at ai_models/phishing_detector.h5")
