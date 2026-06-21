import random,os  # Required to generate random numbers
from flask import Flask, request, render_template_string, session
from flask_mail import Mail, Message

app = Flask(__name__)

# System Settings (Secret key is required to use Flask sessions securely)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Mail Server Settings
app.config['MAIL_SERVER'] = '74.125.142.108'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
mail = Mail(app)

@app.route("/send_otp")
def send_otp():
    # 1. Generate a random 6-digit number string
    otp = str(random.randint(100000, 999999))
    
    # 2. Save it in the user's session data
    session['generated_otp'] = otp
    
    try:
        # 3. Send the OTP via email
        msg = Message(
            subject='Your Security OTP',
            sender='pain.18.pain.18@gmail.com',
            recipients=['mukeshkumarpandian@gmail.com']
        )
        msg.body = f'Your verification code is: {otp}. It is valid for this session only.'
        mail.send(msg)
        
        # 4. Display a quick form to input the OTP
        return render_template_string('''
            <h3>An OTP has been sent to your email.</h3>
            <form action="/verify_otp" method="POST">
                <input type="text" name="user_otp" placeholder="Enter 6-digit OTP" required>
                <button type="submit">Verify OTP</button>
            </form>
        ''')
    except Exception as e:
        return f"Failed to send OTP: {str(e)}"

@app.route("/verify_otp", methods=["POST"])
def verify_otp():
    # 1. Retrieve the true OTP from session and what the user typed from the form
    saved_otp = session.get('generated_otp')
    user_otp = request.form.get('user_otp')
    
    # 2. Check if they match
    if saved_otp and user_otp == saved_otp:
        # Clear the OTP from session so it cannot be reused
        session.pop('generated_otp', None)
        return "<h3>OTP Verification Successful! Welcome.</h3>"
    else:
        return "<h3>Invalid OTP. Please try again.</h3>"

if __name__ == "__main__":
    app.run(debug=True)
