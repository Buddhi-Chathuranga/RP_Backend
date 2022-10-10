

from flask import Blueprint, request
from Controllers.MealPlan import GetAllMealPlan,InsertMealPlan,GetOneMealPlan,UpdateMealPlan,DeleteMealPlan
from Controllers.MealPlanOperation import GetheartMealPlanToUser,GetdiabetesMealPlanToUser
MealPlan = Blueprint("MealPlan",__name__)


@MealPlan.route("/", methods=['GET'])
def GetMealPlan():
    return GetAllMealPlan()



@MealPlan.route('/<ID>',methods=['GET'])
def GetMealPlanByID(ID):
    return GetOneMealPlan(ID)


@MealPlan.route("/", methods=['POST'])
def PostMealPlan():
    request_data = request.get_json();
    return InsertMealPlan(request_data)


@MealPlan.route('/<ID>',methods=['PUT'])
def PutMealPlan(ID):
    request_data = request.get_json();
    return UpdateMealPlan(ID,request_data)


@MealPlan.route('/<ID>', methods=['DELETE'])
def DeleteMealPlanByID(ID):
    return DeleteMealPlan(ID)

@MealPlan.route('/diabetes/<ID>', methods=['Get'])
def GetDiabetesMealPlan(ID):
    return GetdiabetesMealPlanToUser(ID)

@MealPlan.route('/heart/<ID>', methods=['Get'])
def GetHeartMealPlan(ID):
    return GetheartMealPlanToUser(ID)

