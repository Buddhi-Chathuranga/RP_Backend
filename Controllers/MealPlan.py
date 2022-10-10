

from Models.mealPlan import MealPlan 

import json


def InsertMealPlan(request_list):
        try:
                # result = MealPlan(name="Testwith obj", email="test.gmail", password="test123").save()
                resultList = []
                for request_data in request_list:
                        
                        MealPlan01 = MealPlan()
                        MealPlan01.ID = request_data['ID']
                        MealPlan01.MealCategory = request_data['MealCategory']
                        MealPlan01.MealType = request_data['MealType']
                        MealPlan01.CaloryLevel = int(request_data['CaloryLevel'])
                        if('Earlymorning' in request_data):
                                MealPlan01.Earlymorning = request_data['Earlymorning']
                        MealPlan01.Breakfast = request_data['Breakfast']
                        if('AMsnack' in request_data):
                                MealPlan01.AMsnack = request_data['AMsnack']
                        MealPlan01.Lunch = request_data['Lunch']
                        if('PMsnack' in request_data):
                                MealPlan01.PMsnack = request_data['PMsnack']
                        MealPlan01.Dinner = request_data['Dinner']
                        if( 'Eveningsnack'in request_data):
                                MealPlan01.Eveningsnack = request_data['Eveningsnack']
                        if('Contains' in request_data):
                                MealPlan01.Contains = request_data['Contains']
                        result = MealPlan01.save()
                        resultList.append(json.loads(result.to_json()))
               
                return {"result":resultList}
        except Exception as e:
                return {"error":str(e)}
    
def GetAllMealPlan():
        try:
                result = MealPlan.objects()
                return {"result": json.loads(result.to_json())}
        except Exception as e:
                return  {"error":str(e)}
    
def GetOneMealPlan(ID):
        try:
                result = MealPlan.objects(ID=ID)
                return {"result":json.loads(result.to_json())}
        except Exception as e:
                return  {"error":str(e)}

def GetMealPlanByCategory(ID,MealCategory):
        try:
                result = MealPlan.objects(ID=ID, MealCategory=MealCategory)
                return {"result":json.loads(result.to_json())}
        except Exception as e:
                return  {"error":str(e)}
    
def UpdateMealPlan(ID,Updates):
        try:
                result = MealPlan.objects(ID=ID).first()
                if('MealCategory' in Updates):
                        result.MealCategory = Updates['MealCategory']
                if('MealType' in Updates):
                        result.MealType = Updates['MealType']
                if('CaloryLevel' in Updates):
                        result.CaloryLevel = int(Updates['CaloryLevel'])
                if('Earlymorning' in Updates):
                        result.Earlymorning = Updates['Earlymorning']
                if('Breakfast' in Updates):
                        result.Breakfast = Updates['Breakfast']
                if('AMsnack' in Updates):
                        result.AMsnack = Updates['AMsnack']
                if('Lunch' in Updates):
                        result.Lunch = Updates['Lunch']
                if('PMsnack' in Updates):
                        result.PMsnack = Updates['PMsnack']
                if('Dinner' in Updates):
                        result.Dinner = Updates['Dinner']
                if('Eveningsnack' in Updates):
                        result.Eveningsnack = Updates['Eveningsnack']
                if('Contains' in Updates):
                        result.Contains = Updates['Contains']
                result.save()
                return {"result": json.loads(result.to_json())}
        except Exception as e:
                return  {"error":str(e)}
      
    
def DeleteMealPlan(ID):
        try:
                result = MealPlan.objects(ID=ID).first()
                result.delete()
                return {"result":json.loads(result.to_json())}
        except Exception as e:
                return  {"error":str(e)}


        
