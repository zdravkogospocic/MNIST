import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
import keras
import matplotlib.pyplot as plt
import cv2
from tensorflow.keras.utils import load_img

from flask import Flask, redirect, url_for, request
app = Flask(__name__)


model_s = keras.models.load_model("C://Users//Windows//Desktop//MEGATREND//Building_API//bestmodel.h5")



@app.route('/')
def success():
   return render_template("login.html")

@app.route('/', methods=["POST"])
def login():
   imagefile = request.files["imagefile"]
   image_path = "./images/"+ imagefile.filename
   imagefile.save(image_path)
   
   
   # neka_moja_slika=r"C://Users//Windows//Desktop//MEGATREND//Building_API//nula.png"
   test_image = load_img(image_path)
   test_image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)

   test_image = cv2.resize(test_image,(28,28), interpolation = cv2.INTER_LINEAR)

   plt.imshow(test_image.reshape(28, 28),cmap='gray')
   pred = model_s.predict(test_image.reshape(1, 28, 28, 1))
   z = pred.argmax()
   return render_template("drugi.html",prediction = z)

if __name__ == '__main__':
   app.run(debug = True)