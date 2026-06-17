from flask import Flask,request,render_template,redirect
import sqlite3

app = Flask(__name__)

abc=sqlite3.Connection('student.db')
abc.row_factory=sqlite3.Row

abc.execute('create table if not exists student '
'(id integer primary key autoincrement, name text,score integer)')

abc.commit()
abc.close()

@app.route('/add', methods=['POST','GET'])
def stud_add():
    abc=sqlite3.Connection('student.db')
    if request.method=='POST':
        print(request.form)
        name=(request.form.get("name"))
        mark=(request.form.get("score"))
        x="insert into student(name,score) values('{}','{}')".format(name,mark)
        abc.execute(x)
        abc.commit()
        abc.close()
    return render_template("stud_add.html")

@app.route('/view', methods=['GET'])
def stud_view():
    abc=sqlite3.Connection('student.db')
    x="select * from student"
    all_data=abc.execute(x).fetchall()
    abc.commit()
    abc.close()
    return render_template("stud_view.html",data=all_data)

@app.route('/update/<int:id>', methods=['GET','POST'])
def stud_update(id):
    abc=sqlite3.Connection("student.db")
    x="select * from student where id ='{}'".format(id)
    single=abc.execute(x).fetchone()
    if request.method=='POST':
        print(request.form)
        name=(request.form.get("name"))
        mark=(request.form.get("score"))
        x="update student set name='{}',score='{}' where id='{}'".format(name,mark,id)
        abc.execute(x)
        abc.commit()
        abc.close()
        return redirect("/view")
    return render_template("stud_update.html",data=single)

@app.route("/delete/<int:id>")
def stud_delete(id):
    abc=sqlite3.Connection("student.db")
    x="delete from student where id='{}'".format(id)
    abc.execute(x)
    abc.commit()
    abc.close()
    return redirect("/view")

if __name__ == "__main__":
    app.run(debug=True)


    


