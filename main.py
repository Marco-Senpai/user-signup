from flask import Flask, request
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 


page_header = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-5" />
        <meta name="viewport" content="width=device-width, initial scale=1.0 />
        <meta http-equiv="X-UA-Compatible" content="ie=edge" />
        <title>Validation</title>
        <link rel="stylesheet" href="/static/app.css" />
    </head>
    <body>
"""

welcomeMessaging = """
<h1>Wlcome to the page</h1>
<a href="/register">Register</a> """

page_footer = """
    </body>
</html>
"""

register_form = """
<form action="/register" id="form" method="POST">
    <h1>Register Please</h1>
    <label for="username">Username</label>
    <input type="text" name="username" id="username" value="{0}" />
    <p class="error">{1}</p>
    <label for="password">Password</lable>
    <input type="password" name="password" id="password" value="{2}" />
    <p class="error">{3}</p>
    <label for="password">Password Confirmation</label>
    <input type="password" name="password2" id="password2" value="{4}" />
    <p class="error">{5}</p>
    <button type="submit">Register</button>
</form>
"""

@app.route("/register", methods=['POST'])
def register():
    username = cgi.escape(request.form['username'])
    password = cgi.escape(request.form['password'])
    password2 = cgi.escape(request.form['password2'])

    usernameError =""
    passwordError =""
    password2Error =""

    if not username:
        print("no username")
        usernameError = "Username is required to continue"
    if not password:
        passwordError = "Passord is required to continue"
    elif len(password) < 5:
        passwordError = "Password must be at least 5 characters in length"
    else:
        hasNumber = False
        for char in password:
            if char.isdigit():
                hasNumber = True
        if not hasNumber:
            passwordError ="Password must contain number"
    if password != password2:
        password2Error = "Password confirmation must match password"

    if usernameError or passwordError or password2Error:
        print("There is an error!")
        content = page_header + register_form.format(username, usernameError, password, passwordError, password2, password2Error) + page_footer
        return content

    return "Thank you for registering, " + username

@app.route("/")
def index():
    content = page_header + welcomeMessaging + page_footer
    return content

@app.route("/register", methods=['GET'])
def register_page():
    content = page_header + register_form.format("", "", "", "", "", "") + page_footer
    return content

app.run()

