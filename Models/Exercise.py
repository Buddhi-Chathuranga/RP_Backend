from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()
app = Flask(__name__)

# db.connect(host="mongodb+srv://API:r6VbRNTMAmX7AkUM@flask-mongo.srpdnoi.mongodb.net/?retryWrites=true&w=majority")
app.config['MONGODB_SETTINGS'] = {
   'host': 'mongodb+srv://buddhi:1234@database.x8fev.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
}
db.init_app(app)

class Exercise (db.Document):
    ID=db.StringField(required=True, primary_key=True)
    Name = db.StringField(required=True)
    Description=db.StringField(required=True)
    Image = db.StringField(required=True)
    MET = db.FloatField(required=True)