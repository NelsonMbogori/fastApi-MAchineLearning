from typing import Union
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI, File, UploadFile
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import requests

app = FastAPI()



endpoint = 'http://localhost:8505/v1/models/potatoes_model:predict'
CLASS_NAME = ["early blight", "late blight", "healthy"]


@app.get("/ping")
async def ping():
    return "pinging.."#ospf dhcp


def readFileAsImage(data) ->np.ndarray:
    #convert the uploaded file to numpy array
    image = np.array(Image.open(BytesIO(data)))
    return image
    

@app.post("/predict")
async def predict(
    #we are posting an image
    file: UploadFile = File(...)
    
):
    image = readFileAsImage(await file.read())#await helps the system to handle multiple requests
    img_batch = np.expand_dims(image, 0)#remember the model takes a batch image as input but here we are provinding only one image. so we expand dimensions 
    json_data = {
        "instances":img_batch.tolist()
    }
    response = requests.post(endpoint,json=json_data)  
    
    pass




if __name__ == "__main__":
    uvicorn.run(app,host='localhost',port=8080)