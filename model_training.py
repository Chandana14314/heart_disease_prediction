import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score, roc_auc_score

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC

from xgboost import XGBClassifier


class HeartDiseaseTrainer:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            data = pd.read_csv(self.file_path)
            print("Dataset Loaded Successfully")
            return data
        except Exception as e:
            print("Error:", e)

    def preprocess(self, data):

        print("\nChecking Missing Values\n")
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
            random_state=42,
            stratify=y
        )

        return X_train, X_test, y_train, y_test

    def train_models(self, X_train, X_test, y_train, y_test):

        models = {

            "Logistic Regression":
                LogisticRegression(max_iter=1000),

            "KNN":
                KNeighborsClassifier(),

            "Naive Bayes":
                GaussianNB(),

            "Decision Tree":
                DecisionTreeClassifier(),

            "Random Forest":
                RandomForestClassifier(),

            "AdaBoost":
                AdaBoostClassifier(),

            "Gradient Boosting":
                GradientBoostingClassifier(),

            "XGBoost":
                XGBClassifier(use_label_encoder=False,
                              eval_metric='logloss'),

            "SVM":
                SVC(probability=True)
        }

        best_model = None
        best_score = 0

        print("\nTraining Models...\n")

        for name, model in models.items():

            model.fit(X_train, y_train)

            pred = model.predict(X_test)

            prob = model.predict_proba(X_test)[:,1]

            accuracy = accuracy_score(y_test, pred)

            auc = roc_auc_score(y_test, prob)

            print("----------------------------------")
            print(name)
            print("Accuracy :", round(accuracy,4))
            print("ROC AUC :", round(auc,4))

            if auc > best_score:
                best_score = auc
                best_model = model

        print("\nBest Model Selected")
        print(best_model)

        return best_model

    def grid_search(self, model, X_train, y_train):

        if isinstance(model, RandomForestClassifier):

            parameters = {

                "n_estimators":[100,200],

                "max_depth":[5,10,None],

                "min_samples_split":[2,5]

            }

            grid = GridSearchCV(
                estimator=model,
                param_grid=parameters,
                cv=5,
                scoring="roc_auc"
            )

            grid.fit(X_train, y_train)

            print("\nBest Parameters")
            print(grid.best_params_)

            return grid.best_estimator_

        else:

            return model

    def save_model(self, model):

        pickle.dump(model, open("heart_model.pkl","wb"))

        print("\nModel Saved Successfully")


def main():

    trainer = HeartDiseaseTrainer("Heart_Disease_Prediction.csv")

    data = trainer.load_data()

    X_train, X_test, y_train, y_test = trainer.preprocess(data)

    best_model = trainer.train_models(
        X_train,
        X_test,
        y_train,
        y_test
    )

    final_model = trainer.grid_search(
        best_model,
        X_train,
        y_train
    )

    trainer.save_model(final_model)


if __name__ == "__main__":
    main()