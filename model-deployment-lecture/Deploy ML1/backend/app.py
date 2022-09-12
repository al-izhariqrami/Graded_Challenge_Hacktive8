from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from tensorflow import keras

app = Flask(__name__)

datacol = ['tenure','OnlineSecurity','TechSupport','Contract','MonthlyCharges','TotalCharges']

# initiate model & columns
LABEL = ["No", "Yes"]

model = keras.models.load_model('Model_Terbaik.h5')

@app.route("/")
def welcome():
    return "<h3>WELCOME</h3>"

@app.route("/predict", methods=["GET", "POST"])
def predict_titanic():
    if request.method == "POST":
        content = request.json
        try:
            new_data = {'tenure': content['tenure'],
                        'OnlineSecurity': content['OnlineSecurity'],
                        'TechSupport' : content['TechSupport'],
                        'Contract' : content['Contract'],
                        'MonthlyCharges' : content['MonthlyCharges'],
                        'TotalCharges' : content['TotalCharges']}
            new_data = pd.DataFrame([new_data],columns=datacol)
            res = model.predict(new_data)
            res = np.where(res >0.5, 1, 0)
            result = {'result': int(res[0]),
                      'class_name': LABEL[int(res[0])]}
            response = jsonify(success=True,
                               result=result)
            return response, 200
        except Exception as e:
            response = jsonify(success=False,
                               message=str(e))
            return response, 400
    # return dari method get
    return "<p>Silahkan gunakan method POST untuk mode <em>inference model</em></p>"

#app.run(debug=True)