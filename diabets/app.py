from ast import FormattedValue
import re
from flask import Flask, render_template,request
import pickle
import numpy as np


app = Flask(__name__ , template_folder='template')

model = pickle.load(open('clf.pkl','rb'))




@app.route('/')
def home():
    return render_template('index.html')


#To use the predict button in our web-app
@app.route('/predict', methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    pred = model.predict(final_features)
    return render_template('second.html', prediction= pred)





if __name__=="__main__":
    app.run(debug=True)