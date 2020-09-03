#This function loads the model dump and predicts the hours based on input parameters

import joblib
import logging
logging.basicConfig(filename='C:\\Users\\subra\\PycharmProjects\\Group4A_latest\\Logging\\Predictor.log',level=logging.DEBUG)

class predictor:
    def __init__(self):
        pass
    try:
        def predict(df_test):
    #Loading the pipeline dump to transform and PredictorFolder
            model=joblib.load('C:\\Users\\subra\\PycharmProjects\\Group4A_latest\\DatasetFolder\\pipe.ml')

            predicted_hours=model.predict(df_test)
            return predicted_hours
    except:
        print('There is an Error,check if the pickle file exists !!')
logging.debug('Dump Loaded successfully')