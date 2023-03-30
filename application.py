from flask import Flask, render_template, request, Response, url_for, jsonify
import tensorflow as tf
import pickle

from utils import text_preprocessor

file_path = 'ml_model.pickle'
with open(file_path,'rb') as f:
    model = pickle.load(f)

application = Flask(__name__)

# Defining route for home page
@application.route('/')
def index():
    return render_template("index.html")

# Defining route for api
@application.route('/predict_api',methods=['GET','POST'])
def predict_api():
    if request.method == 'POST':

        data = request.json['review']
        preprocessed_data = text_preprocessor(data)
        output = model.predict(preprocessed_data)
        if output>0.5:
            sentiment="Positive"
        else:
            sentiment="Negative"
        return jsonify(sentiment)
    
@application.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        review=request.form['review']
        preprocessed_data = text_preprocessor(review)
        output = model.predict(preprocessed_data)
        if output>0.5:
            sentiment="Positive"
        else:
            sentiment="Negative"
        predictions.append({'review': review, 'sentiment': sentiment})
        return render_template('predictions.html', predictions=predictions)
    return render_template("index.html")

@application.route('/predictions')
def predictions():
    # Render the predictions page with the list of predictions
    return render_template('predictions.html', predictions=predictions)

if __name__=="__main__":
    predictions=[]
    application.run()
        