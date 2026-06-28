import pickle
import numpy as np


class HeartDiseasePredictor:

    def __init__(self):
        try:
            self.model = pickle.load(open("heart_model.pkl", "rb"))
            self.scaler = pickle.load(open("scaler.pkl", "rb"))
        except Exception as e:
            print("Error Loading Model:", e)

    def predict(self,
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
                thal):

        try:

            data = np.array([[

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

            ]])

            scaled_data = self.scaler.transform(data)

            prediction = self.model.predict(scaled_data)[0]

            probability = self.model.predict_proba(scaled_data)[0][1]

            return prediction, probability

        except Exception as e:

            print("Prediction Error :", e)
            return None, None