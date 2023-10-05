from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge,Lasso
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import RandomizedSearchCV
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.exception import CustomException
from src.logger import logging
from src.utils import save_obj
from dataclasses import dataclass
import os, sys
from sklearn.model_selection import train_test_split
from src.utils import evaluate_model


@ dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:

            logging.info("Split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:len(train_array),:-1],
                test_array[:len(train_array),-1]
            )
            models = {
                "Linear Regression": LinearRegression(),
                "Lasso":Lasso(),
                "Ridge":Ridge(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "AdaBoost Regressor": AdaBoostRegressor()
            }

            model_report:dict = evaluate_model(X_train=X_train, y_train=y_train,X_test=X_test, y_test=y_test, models=models)

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]        

            if best_model_score < 0.6:
                raise CustomException("No best model found")
            
            logging.info("Best model found on both training and testing dataset")

            save_obj(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)

            return (
                r2_square,
                best_model_name
            )

        except Exception as e:
            raise CustomException(e, sys)

