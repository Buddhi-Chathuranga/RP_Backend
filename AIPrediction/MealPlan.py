from sklearn.preprocessing import OneHotEncoder
import warnings

warnings.filterwarnings('ignore')
oneH = OneHotEncoder()
import Predictions.Mealplan.heart_patient_meal as hm
import Predictions.Mealplan.diabetes_meal as dm

def Get_diabetes_mealplan(Data):
    diabetes_meal_plan = dm.is_diabetes_mealplan_needed(
    [Data['Gender'], Data['age'], Data['Polyuria'], Data['Polydipsia'], Data['sudden_weight_loss'], Data['weakness'], Data['Polyphagia'], Data['Genital_thrush'], Data['visual_blurring'],
     Data['Itching'], Data['Irritability'], Data['delayed_healing'], Data['partial_paresis'], Data['muscle_stiffness'], Data['Alopecia'], Data['Obesity'],Data['height'],Data['weight'],Data["activity_level"],Data["goals"],Data["foodtype"],Data["risk"] ])
    return diabetes_meal_plan

def Get_heart_patient_mealplan(Data):

    heart_mealplan_output = hm.is_heartpatient_mealplan_needed(
    [Data['gender'], Data['height'], Data['weight'], Data['ap_hi'], Data['ap_lo'], Data['age'], Data['BMI_Class'], Data['MAP_Class'], Data['cholesterol'], Data['gluc'], Data['smoke'], Data['alco'], Data['active'],
     Data['activity_level'], Data['goals'], Data['foodtype'],Data['risk']])
    return heart_mealplan_output 


