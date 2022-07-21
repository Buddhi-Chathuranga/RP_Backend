from ast import And
import collections
from distutils.log import error
from enum import unique
from typing import Collection
import pymongo
from bson import ObjectId 

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
    entireLife100Cigarettes = db.StringField()
    cigarettePerDay = db.StringField()


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
            "entireLife100Cigarettes":self.entireLife100Cigarettes,
            "cigarettePerDay":self.cigarettePerDay,
        }


@app.route('/',methods=['GET'])
def testing():

    return 'Testing Page!'

@app.route('/test',methods=['GET'])
def test():
    request_json = request.get_json()
    value1 = request_json.get('name')
    return 'Testing '+value1


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
                        height = "", age = "", colLev = "", heartRate = "", stroke = "", entireLife100Cigarettes = "", cigarettePerDay = "")
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
        colLev = request_json.get('highBP')
        heartRate = request_json.get('colLev')
        stroke = request_json.get('SBP')
        entireLife100Cigarettes = request_json.get('stroke')
        cigarettePerDay = request_json.get('heAlCo')


        User.objects(id=uid).update(gender = gender, weight = weight, height = height, 
            age = age, colLev = colLev, heartRate = heartRate, stroke =stroke, entireLife100Cigarettes = entireLife100Cigarettes, cigarettePerDay = cigarettePerDay)

        output = {'message' : 'Success'}
        return output
    except Exception as e:
        output = {'message' : str(e)}
        return output



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
    




@app.route('/getUser',methods=['GET'])
def api_each_user():
    request_json = request.get_json()
    user_id = request_json.get('id')
    user_obj = User.objects(id=user_id).first()
    if user_obj:
        return make_response((jsonify(user_obj.to_json())), 200)
    else:
        return make_response('', 404)


@app.route('/userDelete/<user_id>',methods=['DELETE'])
def api_delete_user(user_id: str):
    user_obj = User.objects(id=user_id).first()
    user_obj.delete()
    return make_response('Delete Success', 200)

if __name__ == '__main__':
    app.run()
