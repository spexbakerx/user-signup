from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route('/')
def display_signup():
    return render_template('signup.html')


def is_blank(text):
    if text == '':
        return True



@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if is_blank(username):
        username_error = 'Please enter a username'
    elif ' ' in username:
        username_error = 'Username must not contain any spaces'
        username = ''
    else:
        if len(username) < 3 or len(username) > 20:
            username_error = 'Username must be between 3 and 20 characters'
            username = ''

    if is_blank(password):
        password_error = 'Please enter a password'
    elif ' ' in password:
        password_error = 'Password must not contain any spaces'
        password = ''
    else:
        if len(password) < 3 or len(password) > 20:
            password_error = 'Password must be between 3 and 20 characters'
            password = ''

    if verify != password:
        verify_error = 'Passwords do not match'
        verify = ''

    if ' ' in email:
        email_error = 'Email must not contain any spaces'
        email = ''
    elif email == '':
        email =''
    elif email.count('@') != 1 or email.count('.') != 1:
        email_error = 'Please enter a valid email address'
        email = ''
    else:
        if len(email) < 3 or len(email) > 20:
            email_error = 'Email must be between 3 and 20 characters'
            email = ''

    if not password_error and not username_error and not verify_error and not email_error:
        name = request.form['username']
        return render_template('welcome.html', name=name)
    else:
        return render_template('signup.html', username=username, password=password, verify=verify, email=email, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

@app.route('/welcome', methods=['POST'])
def welcome():
    name = request.form['username']
    return render_template('welcome.html', name=name)


app.run()
