# Imported Libraries
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import warnings
import Predictions.Mealplan.encoders as encoder

warnings.filterwarnings('ignore')
oneH = OneHotEncoder()
import pickle
import dill
import Predictions.Mealplan.health_indicators as health_index


def is_diabetes_mealplan_needed(diabetes_patient_datalist):
    with open('AIModel/MealPlan/diabetes_rf_clf.joblib', 'rb') as io:
        diabetes_rf_clf = dill.load(io)

    Pkl_Filename = "AIModel/MealPlan/diabetes_encoder.pkl"
    with open(Pkl_Filename, 'rb') as file:
        diabetes_encoder = pickle.load(file)

    gender = diabetes_patient_datalist[0]
    age = diabetes_patient_datalist[1]
    age_bin = health_index.get_age_bin(age)

    data = [{'Gender': gender,
             'age_bin': age_bin,
             'Polyuria': diabetes_patient_datalist[2],
             'Polydipsia': diabetes_patient_datalist[3],
             'sudden weight loss': diabetes_patient_datalist[4],
             'weakness': diabetes_patient_datalist[5],
             'Polyphagia': diabetes_patient_datalist[6],
             'Genital thrush': diabetes_patient_datalist[7],
             'visual blurring': diabetes_patient_datalist[8],
             'Itching': diabetes_patient_datalist[9],
             'Irritability': diabetes_patient_datalist[10],
             'delayed healing': diabetes_patient_datalist[11],
             'partial paresis': diabetes_patient_datalist[12],
             'muscle stiffness': diabetes_patient_datalist[13],
             'Alopecia': diabetes_patient_datalist[14],
             'Obesity': diabetes_patient_datalist[15]}]

    height = diabetes_patient_datalist[16]
    weight = diabetes_patient_datalist[17]
    activity_level = diabetes_patient_datalist[18]
    goals = diabetes_patient_datalist[19]
    foodtype = diabetes_patient_datalist[20]
    Risk = diabetes_patient_datalist[21]

    diabetes_data_categorical_columns = encoder.diabetes_data_categorical_columns
    diabetes_encodered_colums = encoder.diabetes_encodered_colums

    try_df = pd.DataFrame(data)
    try_df = pd.DataFrame(diabetes_encoder.transform(try_df[diabetes_data_categorical_columns]).toarray(),
                          columns=diabetes_encodered_colums)
    y_predict = diabetes_rf_clf.predict(try_df)
    x = y_predict.tolist()
    y = x[0]
    if y == 'yes':
        statues = "meal plan need"
    else:
        statues = "No need"

    diabetes_meal_planner = [gender, height, weight, age, activity_level, goals, foodtype, Risk]
    if statues == "meal plan need":
        diabetes_meal_plan = health_index.get_final_meal_plan(diabetes_meal_planner)
    else:
        diabetes_meal_plan = "no_need"

    return diabetes_meal_plan


