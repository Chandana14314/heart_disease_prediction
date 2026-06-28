from flask import Flask, render_template, request
from predict_pipeline import HeartDiseasePredictor

app = Flask(__name__)

predictor = HeartDiseasePredictor()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        age = float(request.form["age"])
        sex = int(request.form["sex"])
        cp = int(request.form["cp"])
        trestbps = float(request.form["trestbps"])
        chol = float(request.form["chol"])
        fbs = int(request.form["fbs"])
        restecg = int(request.form["restecg"])
        thalach = float(request.form["thalach"])
        exang = int(request.form["exang"])
        oldpeak = float(request.form["oldpeak"])
        slope = int(request.form["slope"])
        ca = int(request.form["ca"])
        thal = int(request.form["thal"])

        prediction, probability = predictor.predict(
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal
        )

        if prediction == 1:
            result = "Heart Disease Detected"
        else:
            result = "No Heart Disease"

        probability = round(probability * 100, 2)

        return render_template(
            "result.html",
            prediction=result,
            probability=probability
        )

    except Exception as e:
        return render_template(
            "result.html",
            prediction="Error Occurred",
            probability=0
        )


if __name__ == "__main__":
    app.run(debug=True)