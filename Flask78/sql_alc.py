from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:712221205018@localhost/flask78"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)


class Bike(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20))
    price = db.Column(db.Integer)

with app.app_context():
    db.create_all()


@app.route("/view")
def view_bike():
    all_data=Bike.query.all()
    return render_template ("/bike_view.html",data=all_data)

@app.route("/add", methods = ['GET', 'POST'])
def add_bike():
    if request.method=="POST":
        name=request.form.get("name")
        price=request.form.get("amount")
        x=Bike(name=name,price=price)
        db.session.add(x)
        db.session.commit()
        return redirect("/view")
    return render_template("/bike_add.html")

@app.route("/update/<int:id>", methods=['GET','POST'])
def update_bike(id):
    x=Bike.query.get_or_404(id)
    if request.method=="POST":
        x.name=request.form.get("name")
        x.price=request.form.get("amount")
        db.session.commit()
        return redirect(url_for("view_bike"))
    return render_template("/bike_update.html",data=x)

@app.route("/delete/<int:id>")
def delete_bike(id):
    x=Bike.query.get_or_404(id)
    db.session.delete(x)
    db.session.commit()
    return redirect("/view")

if __name__=="__main__":
    app.run(debug=True)