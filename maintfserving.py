from typing import Union
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import requests
from flask_cors import CORS
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# specify the correct endpoint
endpoint = "http://localhost:8504/v1/models/saved_model:predict"
CLASS_NAME = ["early blight", "late blight", "healthy"]

@app.get("/ping" )
async def ping():
    return "pinging.."


def readFileAsImage(data) ->np.ndarray:
    #convert the uploaded file to numpy array
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = readFileAsImage(await file.read())#await helps the system to handle multiple requests
    img_batch = np.expand_dims(image, 0)#remember the model takes a batch image as input but here we are provinding only one image. so we expand dimensions 
    json_data = {
        "instances": img_batch.tolist()
    }
    response = requests.post(endpoint,json=json_data)
    prediction = np.array(response.json()["predictions"][0])
    
    predicted_class = CLASS_NAME[np.argmax(prediction)]
    confidence = np.max(prediction)

    return {
        "class": predicted_class,
        "confidence": float(confidence)
    }

def application(environ, start_response):
  if environ['REQUEST_METHOD'] == 'OPTIONS':
    start_response(
      '200 OK',
      [
        ('Content-Type', 'application/json'),
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Headers', 'Authorization, Content-Type'),
        ('Access-Control-Allow-Methods', 'POST'),
      ]
    )
    return ''

if __name__ == "__main__":
    uvicorn.run(app,host='localhost',port=8060)