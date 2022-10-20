
import json
from Models.mealPlan import MealPlan
from Models.User import User
from AIPrediction.MealPlan import Get_diabetes_mealplan, Get_heart_patient_mealplan
from Controllers.MealPlan import GetMealPlanByCategory

def GetdiabetesMealPlanToUser(ID):
    try:
        # user = User.objects(id=ID).first()

        Data = {
            'Gender': 'Male',
            'age': 70,
            'Polyuria': 'Yes',
            'Polydipsia': 'Yes',
            'sudden_weight_loss': 'No',
            'weakness': 'Yes',
            'Polyphagia': 'Yes',
            'Genital_thrush': 'Yes',
            'visual_blurring': 'Yes',
            'Itching': 'Yes',
            'Irritability': 'No',
            'delayed_healing': 'Yes',
            'partial_paresis': 'Yes',
            'muscle_stiffness': 'Yes',
            'Alopecia': 'Yes',
            'Obesity': 'Yes',
            # -------------------------------------
            'height': 50,  # feet
            'weight': 50,  # kg
            'activity_level': 'none',
            'goals': 'gain',
            'foodtype': 'Veg',
            'risk': 'Low',
        }
        mealID = Get_diabetes_mealplan(Data)
        return GetMealPlanByCategory(mealID,'Diabetic')
    except Exception as e:
        return {"error": str(e)}


def GetheartMealPlanToUser(ID):
    try:
        # user = User.objects(id=ID).first()
        Data = {
            'gender' : 'female',
            'height' : 5.7,
            'weight' : 85,
            'ap_hi' : 140,
            'ap_lo' : 90,
            'age' : 50,
            'BMI_Class' : 'Obesity',
            'MAP_Class' : 'High',
            'cholesterol' : 'well_above_normal',
            'gluc' : 'normal',
            'smoke' : 'no',
            'alco' : 'no',
            'active' : 'yes',

            # ====================

            'activity_level' : 'none',
            'goals' : 'gain',
            'risk' : 'High',
            'foodtype' : 'Non-Veg'
        }
        mealID = Get_heart_patient_mealplan(Data)
        # print("meal ID - ",mealID)
        # mealplan = MealPlan.objects(ID=mealID)
        # output= json.loads(mealplan.to_json())
        # print("meal plan - ",output)
        return GetMealPlanByCategory(mealID,'Heart')
    except Exception as e:
        return {"error": str(e)}
