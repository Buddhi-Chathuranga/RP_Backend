from ast import And
import collections
from distutils.log import error
from enum import unique
import json
from typing import Collection
from unicodedata import name
import pymongo
from bson import ObjectId 

import sklearn
import pickle

from flask import Flask, request, make_response , jsonify
from flask_mongoengine import MongoEngine

app  = Flask(__name__)

database_name = 'user_db'
DB_URI = 'mongodb+srv://buddhi:1234@database.x8fev.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
app.config['MONGODB_HOST'] = DB_URI

mongo = MongoEngine(app)

db = MongoEngine()
db.init_app(app)

class User(db.Document):
    name = db.StringField()
    phone = db.StringField()
    email = db.StringField(unique=True)
    password = db.StringField()
    gender = db.StringField()
    weight = db.StringField()
    height = db.StringField()
    age = db.StringField()
    colLev = db.StringField()
    heartRate = db.StringField()
    stroke = db.StringField()
    currentSmoker = db.StringField()
    entireLife100Cigarettes = db.StringField()
    cigarettePerDay = db.StringField()
    BPMeds = db.StringField()
    sysBP = db.StringField()
    disBP = db.StringField()
    DifWalk = db.StringField()
    heartRisk = db.StringField()
    diabetesRisk = db.StringField()
    humidity = db.StringField()
    temp = db.StringField()
    stepCount = db.StringField()

    bodyDisoder = db.StringField()
    insulinCount = db.StringField()
    glucose = db.StringField()
    alcoholicsStatus = db.StringField()
    activityStatus = db.StringField()
    bodyFat = db.StringField()
    gripForce = db.StringField()
    SitAndBendForwardLength = db.StringField()
    SitUpsCount = db.StringField()
    BroadJumpLength = db.StringField()

    def to_json(self):
        return  {
            "_id": str(self.pk),
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "password": self.password,
            "gender":self.gender,
            "weight":self.weight,
            "height":self.height,
            "age":self.age,
            "colLev":self.colLev,
            "heartRate":self.heartRate,
            "stroke":self.stroke,
            "currentSmoker":self.currentSmoker,
            "entireLife100Cigarettes":self.entireLife100Cigarettes,
            "cigarettePerDay":self.cigarettePerDay,
            "BPMeds":self.BPMeds,
            "sysBP":self.sysBP,
            "disBP":self.disBP,
            "DifWalk":self.DifWalk,
            "heartRisk":self.heartRisk,
            "diabetesRisk":self.diabetesRisk,
            "humidity": self.humidity,
            "temp":self.temp,
            "stepCount":self.stepCount,
            "bodyDisoder":self.bodyDisoder,
            "insulinCount":self.insulinCount,
            "glucose":self.glucose,
            "alcoholicsStatus":self.alcoholicsStatus,
            "activityStatus":self.activityStatus,
            "bodyFat":self.bodyFat,
            "gripForce":self.gripForce,
            "SitAndBendForwardLength":self.SitAndBendForwardLength,
            "SitUpsCount":self.SitUpsCount,
            "BroadJumpLength":self.BroadJumpLength,
        }


@app.route('/',methods=['GET'])
def testing():
    return 'Testing Page!'

@app.route('/test',methods=['GET'])
def test():
    # request_json = request.get_json()
    # value1 = request_json.get('name')
    return 'Testing '


@app.route('/addNewUser',methods=['POST'])
def addUserFunction():
    try:
        request_json = request.get_json()
        name = request_json.get('name')
        phone = request_json.get('phone')
        email = request_json.get('email')
        password = request_json.get('password')

        user_obj = User.objects(email=email).first()
        if (user_obj):
            data = {
                "Message":"UsedEmail"
            }
            return jsonify(data)
        else: 
            user1 = User(name=name, phone=phone, email=email, password=password, gender = "", weight = "",
                        height = "", age = "", colLev = "", heartRate = "", stroke = "",currentSmoker="", 
                        entireLife100Cigarettes = "", cigarettePerDay = "", BPMeds ="", sysBP ="", disBP="", DifWalk="", 
                        heartRisk="", diabetesRisk="", humidity="", temp="", stepCount="", bodyDisoder="",insulinCount="",
                        glucose="",activityStatus="", bodyFat="", gripForce="", SitAndBendForwardLength="",SitUpsCount="",
                        BroadJumpLength="",)
            user1.save()
            data = {
                'Message': "Success"
            }
            return jsonify(data)

    except Exception as e:
        data = {
            'Message': e
        }
        return jsonify(data)



@app.route('/getUsers',methods=['GET'])
def api_users():
    page = int(request.args.get('page',1))
    limit = int(request.args.get('limit',10))
    movies = User.objects.paginate(page=page, per_page=limit)
    return jsonify(movies), 200



@app.route('/Update',methods=['PUT'])
def update_User():
    try:
        request_json = request.get_json()
        uid = request_json.get('id')
        gender = request_json.get('gender')
        weight = request_json.get('weight')
        height = request_json.get('height')
        age = request_json.get('age')
        colLev = request_json.get('colLev')
        heartRate = request_json.get('heartRate')
        stroke = request_json.get('stroke')
        currentSmoker= request_json.get('currentSmoker')
        entireLife100Cigarettes = request_json.get('entireLife100Cigarettes')
        cigarettePerDay = request_json.get('cigarettePerDay')
        BPMeds = request_json.get('BPMeds')
        sysBP = request_json.get('sysBP')
        disBP = request_json.get('disBP')
        DifWalk = request_json.get('DifWalk')

        bodyDisoder = request_json.get('bodyDisoder')
        insulinCount = request_json.get('insulinCount')
        glucose = request_json.get('glucose')
        alcoholicsStatus = request_json.get('alcoholicsStatus')
        activityStatus = request_json.get('activityStatus')
        bodyFat = request_json.get('bodyFat')
        gripForce = request_json.get('gripForce')
        SitAndBendForwardLength = request_json.get('SitAndBendForwardLength')
        SitUpsCount = request_json.get('SitUpsCount')
        BroadJumpLength = request_json.get('BroadJumpLength')

        # make Heart Diabetics Prediction
        if ( str(request_json.get["gender"]) == "" or str(request_json.get["weight"]) == "" or 
        str(request_json.get["height"]) == "" or str(request_json.get["age"]) == "" or 
        str(request_json.get["colLev"]) == "" or str(request_json.get["heartRate"]) == "" or 
        str(request_json.get["DifWalk"]) == "" or str(request_json.get["sysBP"]) == "" or
         str(request_json.get["stroke"]) == "" or str(request_json.get["currentSmoker"]) == "" or 
         str(request_json.get["entireLife100Cigarettes"]) == "" or 
         str(request_json.get["cigarettePerDay"]) == "" or str(request_json.get["BPMeds"]) == ""  ):
            output = {
                        'Msg' :"reqFill",
                    }
        # else:
        #     Age = int(age)
        #     F_Age = 0
        #     if( 18<=Age<=24 ):
        #         F_Age=1
        #     elif( 25<=Age<=29 ):
        #         F_Age=2
        #     elif( 30<=Age<=34 ):
        #         F_Age=3
        #     elif( 35<=Age<=39 ):
        #         F_Age=4
        #     elif( 40<=Age<=44 ):
        #         F_Age=5
        #     elif( 45<=Age<=49 ):
        #         F_Age=6
        #     elif( 50<=Age<=54 ):
        #         F_Age=7
        #     elif( 55<=Age<=59 ):
        #         F_Age=8
        #     elif( 60<=Age<=64 ):
        #         F_Age=9
        #     elif( 65<=Age<=69 ):
        #         F_Age=10
        #     elif( 70<=Age<=74 ):
        #         F_Age=11
        #     elif( 75<=Age<=79 ):
        #         F_Age=12
        #     elif( Age>=80 ):
        #         F_Age=13

        #     F_currentSmoker = 1
        #     if(currentSmoker=="No"):
        #         F_currentSmoker = 0

        #     F_stroke=1
        #     if(stroke=="No"):
        #         F_stroke=0

        #     BMI = int(weight)/(int(height)*int(height))

        #     F_DifWalk=1
        #     if(DifWalk=="No"):
        #         F_DifWalk=0
            
        #     F_Gender=1
        #     if(gender=="Female"):
        #         F_Gender=0

        #     F_entireLife100Cigarettes=1
        #     if(entireLife100Cigarettes=="No"):
        #         F_entireLife100Cigarettes=0

        #     F_BPMeds=1
        #     if(str(BPMeds)=="No"):
        #         F_BPMeds=0
        

        #     loaded_model_Heart = pickle.load(open('model/Heart.pickle', 'rb'))
        #     reHeart = loaded_model_Heart.predict([[F_Gender, age, F_currentSmoker, int(cigarettePerDay), F_BPMeds, F_stroke, colLev, BMI, int(heartRate)]])
        #     resultHeart = str(reHeart[0])

        #     loaded_model_Diabetes = pickle.load(open('model/Diabetes.pickle', 'rb'))
        #     reDiabetes = loaded_model_Diabetes.predict([[sysBP, int(colLev), BMI, F_entireLife100Cigarettes, F_DifWalk, F_Gender, F_Age]])
        #     resultDiabetes = str(reDiabetes[0])

        #     HeartRisk = resultHeart
        #     DiabetesRisk= resultDiabetes

            #End of make prediction

        User.objects(id=uid).update(gender = gender, weight = weight, height = height, 
            age = age, colLev = colLev, heartRate = heartRate, stroke =stroke, currentSmoker = currentSmoker, 
            entireLife100Cigarettes = entireLife100Cigarettes, cigarettePerDay = cigarettePerDay, BPMeds = BPMeds, 
            sysBP = sysBP, disBP=disBP, DifWalk=DifWalk, bodyDisoder =bodyDisoder , insulinCount =insulinCount , glucose = glucose,
            alcoholicsStatus =alcoholicsStatus , activityStatus = activityStatus, bodyFat = bodyFat, gripForce = gripForce,
            SitAndBendForwardLength = SitAndBendForwardLength,SitUpsCount = SitUpsCount, BroadJumpLength = BroadJumpLength,
             heartRisk="HeartRisk", diabetesRisk="DiabetesRisk")

        output = {'Msg' : 'Success'}
        return output
    except Exception as e:
        output = {'Msg' : str(e)}
        return output


@app.route('/predict',methods=['GET','POST'])
def Predict_d():
    try:
        request_json = request.get_json()
        user_id = request_json.get('id')
        user_obj = User.objects(id=user_id).first()
        
        gender = user_obj["gender"]
        weight = user_obj["weight"]
        height = user_obj["height"]
        age = user_obj["age"]
        colLev = user_obj["colLev"]
        heartRate = user_obj["heartRate"]
        stroke = user_obj["stroke"]
        currentSmoker = user_obj["currentSmoker"]
        entireLife100Cigarettes = user_obj["entireLife100Cigarettes"]
        cigarettePerDay = user_obj["cigarettePerDay"]
        BPMeds = user_obj["BPMeds"]
        sysBP = user_obj["sysBP"]
        DifWalk = user_obj["DifWalk"]
        heartRisk = user_obj["heartRisk"]
        DiabetesRisk = user_obj["diabetesRisk"]


        if ( str(user_obj["gender"]) == "" or str(user_obj["weight"]) == "" or str(user_obj["height"]) == "" or str(user_obj["age"]) == "" or str(user_obj["colLev"]) == "" or str(user_obj["heartRate"]) == "" or str(user_obj["DifWalk"]) == "" or str(user_obj["sysBP"]) == "" or
         str(user_obj["stroke"]) == "" or str(user_obj["currentSmoker"]) == "" or str(user_obj["entireLife100Cigarettes"]) == "" or str(user_obj["cigarettePerDay"]) == "" or str(user_obj["BPMeds"]) == ""  ):
            output = {
                        'Heart' : "reqFill",
                        'Diabetes': "reqFill",
                    }
            return output

        else:
            Age = int(age)
            F_Age = 0
            if( 18<=Age<=24 ):
                F_Age=1
            elif( 25<=Age<=29 ):
                F_Age=2
            elif( 30<=Age<=34 ):
                F_Age=3
            elif( 35<=Age<=39 ):
                F_Age=4
            elif( 40<=Age<=44 ):
                F_Age=5
            elif( 45<=Age<=49 ):
                F_Age=6
            elif( 50<=Age<=54 ):
                F_Age=7
            elif( 55<=Age<=59 ):
                F_Age=8
            elif( 60<=Age<=64 ):
                F_Age=9
            elif( 65<=Age<=69 ):
                F_Age=10
            elif( 70<=Age<=74 ):
                F_Age=11
            elif( 75<=Age<=79 ):
                F_Age=12
            elif( Age>=80 ):
                F_Age=13

            F_currentSmoker = 1
            if(currentSmoker=="No"):
                F_currentSmoker = 0

            F_stroke=1
            if(stroke=="No"):
                F_stroke=0

            BMI = int(weight)/(int(height)*int(height))

            F_DifWalk=1
            if(DifWalk=="No"):
                F_DifWalk=0
            
            F_Gender=1
            if(gender=="Female"):
                F_Gender=0

            F_entireLife100Cigarettes=1
            if(entireLife100Cigarettes=="No"):
                F_entireLife100Cigarettes=0

            F_BPMeds=1
            if(str(BPMeds)=="No"):
                F_BPMeds=0
        

            loaded_model_Heart = pickle.load(open('model/Heart.pickle', 'rb'))
            reHeart = loaded_model_Heart.predict([[F_Gender, age, F_currentSmoker, int(cigarettePerDay), F_BPMeds, F_stroke, colLev, BMI, int(heartRate)]])
            # re = loaded_model.predict([[0, 61, 1, 30.0, 0.0, 0, 225.0, 28.58, 65.0]])
            resultHeart = str(reHeart[0])

            loaded_model_Diabetes = pickle.load(open('model/Diabetes.pickle', 'rb'))
            reDiabetes = loaded_model_Diabetes.predict([[sysBP, int(colLev), BMI, F_entireLife100Cigarettes, F_DifWalk, F_Gender, F_Age]])
            # re = loaded_model.predict([[0, 61, 1, 30.0, 0.0, 0, 225.0, 28.58, 65.0]])
            resultDiabetes = str(reDiabetes[0])

            output = {
                        'Heart' : resultHeart,
                        'Diabetes': resultDiabetes
                    }
            return output 

    except Exception as e:
        output = {
                    'Heart' : "error",
                    'Diabetes': "error",
                    'Error': str(e)
                    
                }
        return output

    # return output




@app.route('/authUser',methods=['POST'])
def get_one_movie():
    request_json = request.get_json()
    email = request_json.get('email')
    password = request_json.get('password')
    user_obj = User.objects(email=email, password=password).first()
    if (user_obj):

        return jsonify(user_obj)
    else:
        data = {
            "_id":{
                "$oid":"Invalid"
                }
        }
        return jsonify(data)
    # return make_response('Valid')
    




@app.route('/getUser',methods=['POST'])
def api_each_user():
    request_json = request.get_json()
    user_id = request_json.get('id')
    user_obj = User.objects(id=user_id).first()
    if user_obj:
        return jsonify(user_obj)
    else:
        data = {
            "_id":{
                "$oid":"Invalid"
                }
        }
        return jsonify(data)


@app.route('/userDelete/<user_id>',methods=['DELETE'])
def api_delete_user(user_id: str):
    user_obj = User.objects(id=user_id).first()
    user_obj.delete()
    return make_response('Delete Success', 200)



@app.route('/stressAddData',methods=['POST'])
def StressAddData():
    try:
        request_json = request.get_json()
        uid = request_json.get('id')
        humidity = request_json.get('humidity')
        temp = request_json.get('temp')
        stepCount = request_json.get('stepCount')
        User.objects(id=uid).update(humidity = humidity, temp = temp, stepCount = stepCount)

        output = {'Msg' : 'Success'}
        return output


    except Exception as e:
        data = {
            'Msg': e
        }
        return jsonify(data)



@app.route('/predictStress',methods=['GET','POST'])
def predictStress():
    try:
        request_json = request.get_json()
        user_id = request_json.get('id')
        user_obj = User.objects(id=user_id).first()
        
        humidity =user_obj["humidity"]
        temp = user_obj["temp"]
        stepCount = user_obj["stepCount"]


        if ( str(user_obj["humidity"]) == "" or str(user_obj["temp"]) == "" 
                or str(user_obj["stepCount"]) == ""  ):
            output = {
                        'Heart' : "reqFill",
                        'Diabetes': "reqFill",
                    }
            return output

        else:
            loaded_model_Heart = pickle.load(open('model/Seliya.pickle', 'rb'))
            reHeart = loaded_model_Heart.predict([[float(humidity), float(temp), int(stepCount)]])
            resultStress = str(reHeart[0])

            output = {
                    'Stress' : resultStress
              }
            return output 

    except Exception as e:
        output = {
                    'Stress' : "error",
                    'Error': str(e)
                    
                }
        return output



if __name__ == '__main__':
    app.run()
