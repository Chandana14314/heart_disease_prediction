import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

import pickle


class DataPreprocessing:

    def __init__(self, file):

        self.file = file

    def preprocess(self):

        data = pd.read_csv(self.file)

        print(data.head())

        print("\nMissing Values\n")

        print(data.isnull().sum())

        X = data.drop("target", axis=1)

        y = data["target"]

        scaler = StandardScaler()

        X = scaler.fit_transform(X)

        pickle.dump(scaler, open("scaler.pkl", "wb"))

        X_train, X_test, y_train, y_test = train_test_split(

            X,

            y,

            test_size=0.2,

            random_state=42

        )

        return X_train, X_test, y_train, y_test