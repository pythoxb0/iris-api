import joblib
import numpy as np
from config import MODEL_PATH, iris_classes

# Load the model
model = joblib.load(MODEL_PATH)

def predict_iris(sepal_length, sepal_width, petal_length, petal_width):
    """
    Predict the iris species and return JSON-friendly dictionary
    """
    X = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(X)[0]
    probabilities = model.predict_proba(X)[0]

    return {
        "predicted_class": iris_classes[prediction],
        "confidence": float(np.max(probabilities)),
        "class_probabilities": {iris_classes[i]: float(prob) for i, prob in enumerate(probabilities)}
    }
