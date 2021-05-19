from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

 
 
#initliazing our flask app, SQLAlchemy and Marshmallow
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/panji'
 
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql6411284:E3f9hQh81l@sql6.freesqldatabase.com:3306/sql6411284'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
 
db = SQLAlchemy(app)
ma = Marshmallow(app)
 


# User Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(10))
    skin_type = db.Column(db.String(30))
    analisa = db.relationship('Analisa', backref='user')
 
 
    def __init__(self, name, age, sex, skin_type):
        self.name = name
        self.age = age
        self.sex = sex
        self.skin_type = skin_type
       
 
class UserSchema(ma.Schema):
    class Meta:
        fields = ("id","name", "age", "sex", "skin_type")
 
 
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Analisa Table
class Analisa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    kode_kulit = db.Column(db.String(50))
    description = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

 
 
    def __init__(self, kode_kulit, description, user):
        self.kode_kulit = kode_kulit
        self.description = description
        self.user = user
        
        
 
class AnalisaSchema(ma.Schema):
    class Meta:
        fields = ("id","kode_kulit", "description", "user_id")
 
 
analisa_schema = AnalisaSchema()
analisas_schema = AnalisaSchema(many=True)

 
""" Endpoint User"""
#adding a user
@app.route('/user', methods = ['POST'])
def add_user():
    name = request.json['name']
    age = request.json['age']
    sex = request.json['sex']
    
 
    my_users = User(name, age, sex, skin_type=None)
    db.session.add(my_users)
    db.session.commit()
 
    return user_schema.jsonify(my_users)


#getting users
@app.route('/user/get', methods = ['GET'])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
 
    return jsonify(result)


#getting particular user
@app.route('/user/<id>/', methods = ['GET'])
def user_details(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

#updating user
@app.route('/user_update/<id>', methods = ['PUT'])
def user_update(id):
    data = request.get_json()
    user = User.query.get(id)
    if data.get("name"):
        user.name= data['name']
    if data.get("age"):
        user.age= data['age'] 
    if data.get("sex"):
        user.sex= data['sex']  

    db.session.commit()
    return user_schema.jsonify(user)


#deleting user
@app.route('/user_delete/<id>/', methods = ['DELETE'])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
 
    return user_schema.jsonify(user)





""" Endpoint Analisa"""
#adding a user
@app.route('/analisa', methods = ['POST'])
def add_analisa():
    kode_kulit = request.json['kode_kulit']
    description = request.json['description']
    name_user = request.json['name_user']
    
    object_user = User.query.filter_by(name=name_user).first()
    my_analisa = Analisa(kode_kulit, description, user=object_user )
    db.session.add(my_analisa)
    db.session.commit()
 
    return analisa_schema.jsonify(my_analisa)

#getting analisa
@app.route('/analisa/get', methods = ['GET'])
def get_anlisa():
    all_analisa = Analisa.query.all()
    result = analisas_schema.dump(all_analisa)
 
    return jsonify(result)

#getting particular anlisa
@app.route('/analisa/<id>', methods = ['GET'])
def analisa_details(id):
    analisa = Analisa.query.get(id)
    return analisa_schema.jsonify(analisa)

#deleting analisis
@app.route('/anlisa_delete/<id>', methods = ['DELETE'])
def analisa_delete(id):
    analisa = Analisa.query.get(id)
    db.session.delete(analisa)
    db.session.commit()
 
    return analisa_schema.jsonify(analisa)

if __name__ == "__main__":
    app.run(debug=True)