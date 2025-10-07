# 🌸 Iris Flower Prediction API

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.101.0-green)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.7.2-orange)

---

## Overview

This is a **Iris Flower Prediction application** built with **FastAPI** and a trained **machine learning model**.  
It allows users to input iris flower features (sepal length, sepal width, petal length, petal width) and predicts the species of the flower: **Setosa, Versicolor, or Virginica**.  

The project includes:  

- **FastAPI backend** with API endpoints  
- **Frontend HTML form** for user interaction  
- **ML model integration** using scikit-learn  
- **Deployment ready** for Render or other cloud platforms  

---

## Features

- Predicts iris flower species based on user input  
- Interactive web form for real-time predictions  
- API endpoint for programmatic access  
- Simple and modular project structure for easy extension  

---

## Project Structure

app/
│
├─ app.py # Main FastAPI app
├─ config.py # Config variables
├─ requirements.txt # Python dependencies
├─ start.sh # Start command for Render
│
├─ model/ # ML model and prediction logic
│ ├─ prediction.py
│ └─ your_model.pkl # Saved ML model
│
├─ schemas/ # Pydantic schemas for input validation
│ └─ userinput.py
│
├─ templates/ # HTML frontend
│ └─ index.html
├─ static/ # CSS / JS / images
│ ├─ style.css
│ └─ script.js
└─ .gitignore # Git ignore file


---

## Installation

1. **Clone the repository**  

```bash
git clone https://github.com/<your-username>/perfect-ml.git
cd perfect-ml
Create and activate a virtual environment

python -m venv myenv
# Windows
myenv\Scripts\activate
# Linux / Mac
source myenv/bin/activate


Install dependencies

pip install -r requirements.txt

Running Locally

Start the FastAPI server:

uvicorn app:app --reload


Open your browser and visit:

http://127.0.0.1:8000/


You can use the form to enter iris flower features and get predictions.

Deployment on Render

Push your project to GitHub.

Create a New Web Service on Render.

Set the following:

Environment: Python 3.12

Build Command: pip install -r requirements.txt

Start Command: ./start.sh
or
uvicorn app:app --host 0.0.0.0 --port $PORT

Deploy and visit your live URL.

Usage

Form Input Example:

Feature	Value
Sepal Length	5.1
Sepal Width	3.5
Petal Length	1.4
Petal Width	0.2

Prediction Output Example:

{
  "prediction": "setosa"
}

Author

Sahil Kumar

GitHub: https://github.com/pythoxb

LinkedIn: https://linkedin.com/in/pythoxb

License

This project is licensed under the MIT License.


---

If you want, I can also **add badges** for:  

- Live demo on Render  
- ML model accuracy  
- Python & FastAPI version  

…to make it look more **professional and portfolio-ready**.  

Do you want me to add those badges?
