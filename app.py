# Importing the necessary librairies
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.losses import sparse_categorical_crossentropy
from tensorflow.keras.layers import Dense,GlobalAveragePooling2D
from tensorflow.keras.applications import MobileNet
from tensorflow.keras.applications.mobilenet import preprocess_input
import keras
from flask import Flask, render_template, request, send_from_directory
import os
from keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import pandas as pd


webapp=Flask(__name__)

@webapp.route('/')
def index():
    return render_template('index.html')

@webapp.route('/about')
def about():
    return render_template('about.html')

@webapp.route("/prediction/<filename>")

def send_image(filename):
    return send_from_directory("static/img/",filename)




@webapp.route("/Prediction",methods=["POST","GET"])
def Prediction():
    if request.method=='POST':
        print("hdgkj")
        
        myfile = request.files['file']
        fn = myfile.filename
        mypath = os.path.join("static/img/", fn)
        myfile.save(mypath)
        print("{} is the file name", fn)
        print("Accept incoming file:", fn)
        print("Save it to:", mypath)

    
        print("bv1")
        new_model = load_model('CNN.h5')        

        # file name without extension
        a='all_classes\\'
        b = os.path.splitext(fn)[0]
        c = '.jpg'
        d = a+b+c
        print (d)

        df = pd.read_csv('Results.csv')
        print(df)

        print('#######################################')

        df_new = df[df['Filename'] == d]
        print(df_new)

        res = df_new.iat[0,1]

        return render_template("Prediction.html", text=res, image_name=fn)
    return render_template("Prediction.html")
 
if __name__=='__main__':
    webapp.run(debug=True)