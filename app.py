from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from schemas.userinput import IrisInput
from model.prediction import predict_iris
from config import MODEL_VERSION

app = FastAPI(title="Iris Flower Prediction API")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(data: IrisInput):
    return predict_iris(
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    )
