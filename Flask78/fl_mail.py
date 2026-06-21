from flask import Flask,request,redirect
from flask_mail import Mail,Message

app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USERNAME']='pain.18.pain.18@gmail.com'
app.config['MAIL_PASSWORD']='johw evew dtqm nyrx'
app.config['MAIL_USE_TLS']=True
mail = Mail(app)

@app.route("/send")
def send_mail():
    msg = Message('Hello', sender = 'pain.18.pain.18@gmail.com',
                  recipients = ['mukeshkumarpandian@gmail.com'])
    msg.body = 'greetings siva'
    mail.send(msg)
    return "mail sent successfully"

if __name__ == "__main__":
    app.run(debug=True)