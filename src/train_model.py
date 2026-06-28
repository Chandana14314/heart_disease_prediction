import pickle

from sklearn.ensemble import RandomForestClassifier


class TrainModel:

    def train(self, X_train, y_train):

        model = RandomForestClassifier()

        model.fit(X_train, y_train)

        pickle.dump(

            model,

            open("heart_model.pkl", "wb")

        )

        print("Model Saved Successfully")