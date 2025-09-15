import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application



## import logistic regressor model and standard scaler pickle
logistic_model=pickle.load(open('models/logistic.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

## Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        pclass=float(request.form.get('pclass','0'))
        sex= float(request.form.get('sex','0'))
        age = float(request.form.get('age','0'))
        sibsp= float(request.form.get('sibsp','0'))
        parch= float(request.form.get('parch','0'))
        fare= float(request.form.get('fare','0'))
        who= float(request.form.get('who','0'))
        adult_male= float(request.form.get('adult_male','0'))
        embark_town= float(request.form.get('embark_town','0'))
        alone= float(request.form.get('alone','0'))
        

        new_data_scaled=standard_scaler.transform([[pclass,sex,age,sibsp,parch, fare, who, adult_male, embark_town, alone]])
        result=logistic_model.predict(new_data_scaled)

        return render_template('home.html',result=result[0])

    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)