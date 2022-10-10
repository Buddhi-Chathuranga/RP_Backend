
from flask import Flask
from flask_mongoengine import MongoEngine


db = MongoEngine()
app = Flask(__name__)

# db.connect(host="mongodb+srv://API:r6VbRNTMAmX7AkUM@flask-mongo.srpdnoi.mongodb.net/?retryWrites=true&w=majority")
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
    BP = db.StringField()
    DifWalk = db.StringField()
    heartRisk = db.StringField()
    diabetesRisk = db.StringField()

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
            "BP":self.BP,
            "DifWalk":self.DifWalk,
            "heartRisk":self.heartRisk,
            "diabetesRisk":self.diabetesRisk,
        }
