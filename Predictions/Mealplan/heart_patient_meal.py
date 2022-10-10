# Imported Libraries
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import warnings
warnings.filterwarnings('ignore')
oneH = OneHotEncoder()
import pickle
import dill
import Predictions.Mealplan.encoders as encoder
import Predictions.Mealplan.health_indicators as health_index


def is_heartpatient_mealplan_needed(heart_patient_datalist):
    gender = heart_patient_datalist[0]

    height = heart_patient_datalist[1]
    height_cm = int(round(30.48 * height, 0))

    weight = heart_patient_datalist[2]
    weight_kg = int(round(weight, 0))

    systolic_blood_pressure = int(round(heart_patient_datalist[3], 0))

    diastolic_blood_pressure = int(round(heart_patient_datalist[4], 0))

    bmi_state = health_index.cal_bmi_statues(heart_patient_datalist[1], heart_patient_datalist[2])

    map_state = health_index.cal_mean_Arterial_Pressure(systolic_blood_pressure, diastolic_blood_pressure)

    age = heart_patient_datalist[5]
    age_bin = health_index.get_age_bin(age)

    activity_level = heart_patient_datalist[13]

    goals = heart_patient_datalist[14]

    foodtype = heart_patient_datalist[15]
    Risk = heart_patient_datalist[16]

    with open('AIModel/MealPlan/heart_rf_clf.joblib', 'rb') as io:
        heart_clf = dill.load(io)

    Pkl_Filename = "AIModel/MealPlan/heart_encoder.pkl"
    with open(Pkl_Filename, 'rb') as file:
        heart_encoder = pickle.load(file)

    cardiovascular_data_categorical_columns = encoder.cardiovascular_data_categorical_columns
    cardiovascular_encodered_colums = encoder.cardiovascular_encodered_colums

    data = [{'gender': gender,
             'height': height_cm,
             'weight': weight_kg,
             'ap_hi': systolic_blood_pressure,
             'ap_lo': diastolic_blood_pressure,
             'age_bin': age_bin,
             'BMI_Class': bmi_state,
             'MAP_Class': map_state,
             'cholesterol': heart_patient_datalist[8],
             'gluc': heart_patient_datalist[9],
             'smoke': heart_patient_datalist[10],
             'alco': heart_patient_datalist[11],
             'active': heart_patient_datalist[12]}]

    try_df = pd.DataFrame(data)
    try_df = pd.DataFrame(heart_encoder.transform(try_df[cardiovascular_data_categorical_columns]).toarray(),
                          columns=cardiovascular_encodered_colums)
    y_predict = heart_clf.predict(try_df)
    x = y_predict.tolist()
    y = x[0]
    if y == 'yes':
        statues = "meal plan need"
    else:
        statues = "No need"

    meal_planner= [gender, height, weight,age, activity_level, goals, foodtype,Risk]
    if statues == "meal plan need":
        meal_plan = health_index.get_final_meal_plan(meal_planner)
    else:
        meal_plan = "no_need"

    return meal_plan
