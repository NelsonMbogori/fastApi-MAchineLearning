from typing import Union
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI, File, UploadFile
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()



MODEL = tf.keras.models.load_model("./models/1/potatoesvA.hdf5")# load the pre trained model we saved
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
    predictions = MODEL.predict(img_batch)
    predicted_class = CLASS_NAME[np.argmax(predictions[0])]#take the prediction with the highest probability
    confidence = np.max(predictions[0])#the confidence is the probability of the pred
    return {
        'class':predicted_class,
        'confidence':float(confidence)
    }
    




if __name__ == "__main__":
    uvicorn.run(app,host='localhost',port=8080)