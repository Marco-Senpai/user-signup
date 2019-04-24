from flask import Flask, request, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route("/register", methods=['POST'])
def register():
    username = cgi.escape(request.form['username'])
    password = cgi.escape(request.form['password'])
    password2 = cgi.escape(request.form['password2'])
    email = cgi.escape(request.form['email'])

    usernameError =""
    passwordError =""
    password2Error =""
    emailError =""

    if not username:
        print("no username")
        usernameError = "Username is required to continue"
    elif len(username) < 3:
        usernameError = "Username must be at least 3 characters in length"
    elif ' ' in username:
        usernameError = "Username can not contain spaces"
    if not password:
        passwordError = "Passord is required to continue"
    elif len(password) < 3:
        passwordError = "Password must be at least 3 characters in length"
    elif ' ' in password:
        passwordError = "Password can not contain spaces"
    
    if '@' not in email or '.' not in email:
        emailError = "Must include a valid email"
    
    else:
        hasNumber = False
        for char in password:
            if char.isdigit():
                hasNumber = True
        if not hasNumber:
            passwordError ="Password must contain number"
    if password != password2:
        password2Error = "Password confirmation must match password"

    if usernameError or passwordError or password2Error or emailError:
        print("There is an error!")
        return render_template('welcome.html',username=username, usernameError=usernameError, password=password, passwordError=passwordError, password2=password2, password2Error=password2Error, emailError=emailError)
    

    return "Thank you for registering, " + username

    

@app.route("/")
def index():

    return render_template('base.html')


@app.route("/register", methods=['GET'])
def register_page():
    return render_template('welcome.html', username='', usernameError='', password='', passwordError='', password2='', password2Error='', email='', emailError='')

app.run()


