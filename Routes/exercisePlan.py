from flask import Blueprint,request
from Controllers.ExercisePlan import GetAllExercisePlan,InsertExercisePlan,GetOneExercisePlan,UpdateExercisePlan,DeleteExercisePlan

ExercisePlan=Blueprint("ExercisePlan",__name__)

@ExercisePlan.route("/", methods=['GET'])
def GetExercisePlan():
    return GetAllExercisePlan()


@ExercisePlan.route('/<ID>',methods=['GET'])
def GetExercisePlanByID(ID):
    return GetOneExercisePlan(ID)


@ExercisePlan.route("/",methods=['POST'])
def PostExercisePlan():
    request_data = request.get_json();
    return InsertExercisePlan(request_data)


@ExercisePlan.route('/<ID>', methods=['PUT'])
def PutExercisePlan(ID):
    request_data = request.get_json();
    return UpdateExercisePlan(ID,request_data)


@ExercisePlan.route('/<ID>', methods=['DELETE'])
def DeleteExercisePlanByID(ID):
    return DeleteExercisePlan(ID)