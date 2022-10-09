

from flask import Flask
from flask_mongoengine import MongoEngine


db = MongoEngine()
app = Flask(__name__)

# db.connect(host="mongodb+srv://API:r6VbRNTMAmX7AkUM@flask-mongo.srpdnoi.mongodb.net/?retryWrites=true&w=majority")
app.config['MONGODB_SETTINGS'] = {
   'host': 'mongodb+srv://buddhi:1234@database.x8fev.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
}
db.init_app(app)

MealCategory=('Heart','Diabetic')
MealType = ('veg','non-veg')

class MealPlan(db.Document):
    ID = db.StringField(required=True, primary_key=True)
    MealCategory= db.StringField(required=True, choices=MealCategory)
    MealType = db.StringField(required=True, choices=MealType)
    CaloryLevel= db.IntField()
    Earlymorning = db.ListField(db.StringField())
    Breakfast= db.ListField(db.StringField(), required=True)
    AMsnack = db.ListField(db.StringField())
    Lunch= db.ListField(db.StringField(), required=True)
    PMsnack = db.ListField(db.StringField())
    Dinner = db.ListField(db.StringField(), required=True)
    Eveningsnack = db.ListField(db.StringField())
    Contains = db.ListField(db.StringField())

