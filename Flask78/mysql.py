from flask import Flask, request, render_template, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "712221205018"
app.config["MYSQL_DB"] = "flask78"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

@app.route('/view')
def get_emp():
    abc = mysql.connection.cursor()
    x = "select * from emp"
    abc.execute(x)
    result = abc.fetchall()
    abc.close()
    return render_template('emp_view.html', data=result)

@app.route('/add', methods=['GET', 'POST'])
def add_emp():
    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form.get('name')
        salary = request.form.get('salary')
        abc = mysql.connection.cursor()
        x="insert into emp values('{}','{}','{}')".format(id,name,salary)
        abc.execute(x)
        mysql.connection.commit()
        abc.close()
        return redirect('/view')
    return render_template('emp_add.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_emp(id):

    if request.method == 'POST':
        name = request.form.get('name')
        salary = request.form.get('salary')
        abc= mysql.connection.cursor()
        x="update emp set name='{}',salary='{}' where id='{}'".format(name,salary,id)
        abc.execute(x)
        mysql.connection.commit()
        abc.close()
        return redirect('/view')
    
    abc = mysql.connection.cursor()
    x = "select * from emp where id = '{}'".format(id)
    abc.execute(x)
    single = abc.fetchone()
    abc.close()
    return render_template('emp_update.html',data=single)    

@app.route('/delete/<int:id>')
def delete_emp (id):
    abc=mysql.connection.cursor()
    x = "delete from emp where id = %s" # better than format() for sql injections
    abc.execute(x,(id,))
    mysql.connection.commit()
    abc.close()
    return redirect("/view")

if __name__ == "__main__":
    app.run(debug=True)