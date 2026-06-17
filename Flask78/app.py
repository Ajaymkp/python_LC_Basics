from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/abc")
def func():
    return "hi helo"

@app.route("/<num>")
def sh(num):
    return f"int {num}"

@app.route("/<int:num>")
def show(num):
    return f"num {num}"

@app.route("/a")
def abc():
    return "<h1>hi helo</h1>"

# @app.route("/")
# def html():
#     name = "Sanji"
#     num = 10
#     return render_template("index.html",data=name,n=num)

app.route("/<name>/<int:age>")
def detail(name,age):
    return f"name is {name} age is {age}"

#http://127.0.0.1:5000/detail?name=anbu&age=25&reg=1818

@app.route("/detail")
def detaill():
    a=request.args.get("name")
    b=request.args.get("age")
    c=request.args.get("reg")
    return f" my name is {a} age is {b} regester num {c}"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/contact")
def contacts():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/index")
def service():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
