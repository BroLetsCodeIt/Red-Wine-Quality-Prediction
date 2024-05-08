from flask import *
import os 
import numpy as np 
import pandas as pd 
from src.mlProject.pipeline.prediction import *

app = Flask(__name__)

# we need to create the two route - 
# 1 . training route 
# 2. prediction route

@app.route('/')
def HomePage():
    return render_template('landing.html')


@app.route('/train' , methods=['GET'])
def training() :
    os.system('python main.py')
    return "Training successfull"

@app.route('/forming')
def forming():
    return render_template('index.html')


@app.route('/predict' , methods=['GET', 'POST'])
def Predict():
    if request.method == 'POST':
        try: 

            # get the each and every field value in variable here

            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])

            data = [fixed_acidity , volatile_acidity , citric_acid , residual_sugar , chlorides , free_sulfur_dioxide , total_sulfur_dioxide , density , pH , sulphates , alcohol]

            data = np.array(data).reshape(1,11)

            obj = PredictionPipeline()
            predict = obj.predict(data)
            predicted_val  = predict[0]
            return render_template('results.html' , prediction = str(predicted_val))
        
        except Exception as e : 
            print("The exception message is ",e)
            return "something went wrong"

    else : 
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=3234)
