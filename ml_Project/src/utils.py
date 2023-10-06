import sys, os
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
import pickle


def save_obj(file_path, obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys) 
    

def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report:dict = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            # param = list(params.values())[i]
            # gs = GridSearchCV(model, param_grid=param,cv=3,
                              
            # verbose=False, scoring="neg_mean_squared_error" )

            # gs.fit(X_train, y_train)

            # model = gs.best_estimator_
                        # or
            model.fit(X_train,y_train)
            # y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            # train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            # report[list(models)[i]] = train_model_score
            
            report[list(models)[i]] = test_model_score

        return report
    
    except Exception as e:
        raise CustomException(e, sys)
    


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj) 
    except Exception as e:
        raise CustomException(e, sys)