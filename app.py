from flask import Flask, render_template, request
import numpy as np
import os

app = Flask(__name__)

def get_pipeline():
    from src.mlProject.pipeline.predictions import PredictionPipeline
    return PredictionPipeline()


@app.route('/', methods=['GET'])
def homePage():
    return render_template("index.html")


@app.route('/train', methods=['GET'])
def training():
    
    os.system("python main.py")
    return "Training Successful!"


@app.route('/predict', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            data = np.array([
                fixed_acidity, volatile_acidity, citric_acid,
                residual_sugar, chlorides, free_sulfur_dioxide,
                total_sulfur_dioxide, density, pH, sulphates, alcohol
            ]).reshape(1, 11)

            pipeline = get_pipeline()
            predict = pipeline.predict(data)

            return render_template('results.html', prediction=str(predict))

        except Exception as e:
            print("Error:", e)
            return "Prediction error occurred"

    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)