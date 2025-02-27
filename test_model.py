import tensorflow as tf
import numpy as np
from tensorflow.keras.datasets import mnist

# Load the trained model
model = tf.keras.models.load_model("sudoku_digit_recognition.h5")

# Load MNIST test dataset
(_, _), (x_test, y_test) = mnist.load_data()

# Normalize and reshape data
x_test = x_test / 255.0
x_test = x_test.reshape(-1, 28, 28, 1)

# Evaluate model performance
loss, accuracy = model.evaluate(x_test, y_test, verbose=2)
print(f"Model Test Accuracy: {accuracy * 100:.2f}%")

# Predict first 10 images
predictions = model.predict(x_test[:10])
predicted_labels = np.argmax(predictions, axis=1)

print("Predicted labels:", predicted_labels)
print("Actual labels:   ", y_test[:10])
