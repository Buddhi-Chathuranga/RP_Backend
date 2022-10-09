from flask import Blueprint,request
from Controllers.Exercise import GetAllExercise,InsertExercise,GetOneExercise,UpdateExercise,DeleteExercise

Exercise=Blueprint("Exercise",__name__)

@Exercise.route("/" ,methods=['GET'])
def GetExercise():
    return GetAllExercise()

@Exercise.route('/<ID>', methods=['GET'])
def GetExerciseByID(ID):
    return GetOneExercise(ID)

@Exercise.route("/", methods=['POST'])
def PostExercise():
    request_data = request.get_json();
    return InsertExercise(request_data)
   
@Exercise.route('/<ID>',methods=['PUT'])
def PutExercise(ID):
    request_data = request.get_json();
    return  UpdateExercise(ID,request_data)

@Exercise.route('/<ID>', methods=['DELETE'])
def DeleteExerciseByID(ID):
    return DeleteExercise(ID)


