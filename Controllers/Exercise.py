
from Models.Exercise import Exercise

import json

def InsertExercise(request_list):
        try:
                if request_list:
                        Exercise01 = Exercise()
                        Exercise01.ID = request_list['ID']
                        Exercise01.Name = request_list['Name']
                        Exercise01.Description = request_list['Description']
                        Exercise01.Image = request_list['Image']
                        Exercise01.MET = request_list['MET']
                        result = Exercise01.save()
                        resultList = json.loads(result.to_json())
                return {"result":resultList}
        except Exception as e:
                return  {"error":str(e)}

def GetAllExercise():
        try:
                result = Exercise.objects()
                return {"result":json.loads(result.to_json())}
        except Exception as e:
                return  {"error":str(e)}

def GetOneExercise(ID):
        try:
                result = Exercise.objects(ID=ID).first()
                return {"result":json.loads(result.to_json())}
        except Exception as e:
                return  {"error":str(e)}

def UpdateExercise(ID,Updates):
        try:
                result = Exercise.objects(ID=ID).first()
                if('Name' in Updates):
                        result.Name = Updates['Name']
                if('Description' in Updates):
                        result.Description = Updates['Description']
                if('Image' in Updates):
                        result.Image = Updates['Image']
                result.save()
                return {"result":json.loads(result.to_json())}
        except Exception as e:
                return  {"error":str(e)}

def DeleteExercise(ID):
        try:
                result = Exercise.objects(ID=ID).first()
                result.delete()
                return {"result":json.loads(result.to_json())}
        except Exception as e:
                return  {"error":str(e)}