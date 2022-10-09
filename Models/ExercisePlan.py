from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()
app = Flask(__name__)

# db.connect(host="mongodb+srv://API:r6VbRNTMAmX7AkUM@flask-mongo.srpdnoi.mongodb.net/?retryWrites=true&w=majority")
app.config['MONGODB_SETTINGS'] = {
   'host': 'mongodb+srv://buddhi:1234@database.x8fev.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
}
db.init_app(app)

EType = ('Aerobic_exercises','Anerobic_exercises','Streching_exercises')

class ExercisePlan(db.Document):
    ID = db.StringField(required=True)
    ExerciseType = db.StringField(required=True,choices=EType)
    ExerciseList= db.ListField(db.StringField(), required=True)
    