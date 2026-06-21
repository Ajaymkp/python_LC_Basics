from flask import Flask,request,redirect,jsonify
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
from sqlite import sqlite3

app=Flask(__name__)
api=Api(app)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///student.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False


db=SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    actor = db.Column(db.String(20))

with app.app_context():
    db.create_all()

class Movie_add_view(Resource):
    def post(self):
        print(request.json)
        name=request.json['name']
        actor=request.json['actor']
        
        x=Movie(name=name,actor=actor)
        db.session.add(x)
        db.session.commit()
        return jsonify(
            {"msg" : "Data added"}
        )
    def get(self):
        all_data = Movie.query.all()
        data=[]
        for i in all_data:
            z={"id":i.id,"name":i.name,"actor":i.actor}
            data.append(z)
        return jsonify(data)

class Movie_update_delete (Resource):
    def get(self,id):
        abc = Movie.query.get(id)
        data = {"id":abc.id,"name":abc.name,"actor":abc.actor}
        return jsonify(data)
    def put(self,id):
        abc = Movie.query.get_or_404(id)
        abc.name=request.json['name']
        abc.actor=request.json['actor']
        db.session.commit()
        return jsonify({"msg" : "Data updated"})    
    def patch(self,id):
        abc = Movie.query.get_or_404(id)
        abc.name=request.json['name']
        abc.actor=request.json['actor']
        db.session.commit()
        return jsonify({"msg" : "Data updated"}) 
    def delete(self,id):
        abc = Movie.query.get_or_404(id)
        db.session.delete(abc)
        db.session.commit()    
        return jsonify({"msg":"data deleted"})     

api.add_resource(Movie_add_view,"/view/")
api.add_resource(Movie_update_delete,"/view/<int:id>/")


if __name__ == "__main__":
    app.run(debug=True)