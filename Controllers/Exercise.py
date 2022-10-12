
from Models.Exercise import Exercise
from flask import jsonify
import json

def InsertExercise(request_list):
        try:
                resultList = []
                for request_data in request_list:
                        if request_data:
                                Exercise01 = Exercise()
                                Exercise01.ID = request_data['ID']
                                Exercise01.Name = request_data['Name']
                                if('Description' in request_data):
                                        Exercise01.Description = request_data['Description']
                                Exercise01.Image = request_data['Image']
                                Exercise01.MET = request_data['MET']
                                result = Exercise01.save()
                                resultList.append(json.loads(result.to_json()))
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
                if(result):
                       
                        return {"result":json.loads(result.to_json())}
                else:
                        return {"result":None}
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