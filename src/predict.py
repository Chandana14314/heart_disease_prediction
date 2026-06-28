import pickle
import numpy as np

from src.exception import CustomException


class PredictPipeline:

    def __init__(self):

        self.model = pickle.load(open("heart_model.pkl", "rb"))
        self.scaler = pickle.load(open("scaler.pkl", "rb"))

    def predict(self, data):

        try:

            scaled = self.scaler.transform(data)

            prediction = self.model.predict(scaled)

            probability = self.model.predict_proba(scaled)

            return prediction, probability

        except Exception as e:

            raise CustomException(e)