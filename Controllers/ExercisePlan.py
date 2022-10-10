from Models.ExercisePlan import ExercisePlan
from Controllers.Exercise import GetOneExercise
import json

def InsertExercisePlan(request_list):
        try:
                resultList = []
                for request_data in request_list:
                        if request_data:
                                ExercisePlan01 = ExercisePlan()
                                ExercisePlan01.ID = request_data['ID']
                                ExercisePlan01.ExerciseType = request_data['ExerciseType']
                                ExercisePlan01.ExerciseList = request_data['ExerciseList']
                                result = ExercisePlan01.save()
                                resultList.append(json.loads(result.to_json()))
                return {"result":resultList}
        except Exception as e:
                return  {"error":str(e)}

def GetAllExercisePlan():
        try:
                result = ExercisePlan.objects()
                for i in result.to_json():
                        execise=[] 
                        print("ExercisePlan",i)
                        for j in i['ExerciseList']:
                        #    execise.append(GetOneExercise(j))
                           print("Exercise",j)
                           j= j.replace(j,json.dumps(GetOneExercise(j)))
                           execise.append(j)
                        print("ReplaceExercise",execise)
                        i['ExerciseList']=execise
                return {"result":json.loads(result)}
        except Exception as e:
                return  {"error":str(e)}

def GetOneExercisePlan(ID):
        try:
                result = ExercisePlan.objects(ID=ID).first()
                return {"result":json.loads(result.to_json())}
        except Exception as e:
                return  {"error":str(e)}

def UpdateExercisePlan(ID,Updates):
        try:
                result = ExercisePlan.objects(ID=ID).first()
                if('ExerciseType' in Updates):
                        result.ExerciseType = Updates['ExerciseType']
                if('ExerciseList' in Updates):
                        result.ExerciseList = Updates['ExerciseList']
                if('MET' in Updates):
                        result.MET = Updates['MET']
                result.save()
                return {"result":json.loads(result.to_json())}
        except Exception as e:
                return  {"error":str(e)}

def DeleteExercisePlan(ID):
        try:
                result = ExercisePlan.objects(ID=ID).first()
                result.delete()
                return {"result":json.loads(result.to_json())}
        except Exception as e:
                return  {"error":str(e)}

                