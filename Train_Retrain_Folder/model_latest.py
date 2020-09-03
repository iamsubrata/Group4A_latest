import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import joblib
from sklearn.compose import make_column_transformer
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline

class train_retrain:
    def __init__(self):
        pass

    def re_train(df_new):
        try:
            df_old = pd.read_csv('./Train_Data.csv')
            df_old.rename(columns={'Reason for absence': 'R_code', 'Transportation expense': 'Transportation expense',
                                   'Distance from Residence to Work': 'Office Distance', 'Age': 'Age',
                                   'Body mass index': 'Body mass index'}, inplace=True)
            df_old_sub = df_old[
                ['R_code', 'Transportation expense', 'Office Distance', 'Age', 'Body mass index', 'Absnt_hr_estimate']]
            df_retrain = pd.concat([df_old_sub, df_new], ignore_index=True, sort=False)
            print('Provided data added successfully to the original data')
            df_retrain.to_csv('C:\\Users\\subra\\PycharmProjects\\Group4A_latest\\Train_Data.csv', index=False)
            # Spliting dependent & independent data
            X = df_retrain.drop('Absnt_hr_estimate', axis=1)
            y = df_retrain['Absnt_hr_estimate']
            # encoding for categorical variables
            column_trans = make_column_transformer((OneHotEncoder(sparse=False), ['R_code']), remainder='passthrough')
            X = column_trans.fit_transform(X)

            # Instantiating classifier
            clf_rf = RandomForestClassifier(n_estimators=2000, random_state=42)
            clf_rf.fit(X, y)
            print('Model fitted successfully to the new data')

            # Creating a pipeline to avoid rework
            pipe = make_pipeline(column_trans, clf_rf)

            # Creating a serialized version of model for reuse
            joblib.dump(pipe, '../DatasetFolder/pipe.ml')
            print('successfull creation of serialized model object')
        except:
            print('Check the model building & retraing steps')



        return ('Model re trained successfully')













