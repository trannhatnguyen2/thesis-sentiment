from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from loguru import logger

from model.model import predict_pipeline
from preprocess.preprocessing import preprocessing

cache = {}

app = FastAPI()

class TextIn(BaseModel):
    review: str

class PredictionOut(BaseModel):
    sentiment: str

@app.get('/')
def home():
    return {'text': "Nguyen's Thesis"}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):

    if payload.review != '':
        review_handled = preprocessing(payload.review)
        sentiment = predict_pipeline(review_handled)

    return {"sentiment": sentiment}


if __name__ == '__main__':
    uvicorn.run(app)