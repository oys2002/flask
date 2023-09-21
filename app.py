from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__)


users = {
    'user1': {'password': 'password1', 'email': 'user1@example.com'},
    'user2': {'password': 'password2', 'email': 'user2@example.com'}
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')

    if username in users and users[username]['password'] == password:
        email = users[username]['email']
        return f'Logged in as {username} (Email: {email})'
    else:
        return 'Invalid credentials. Please try again.'


@app.route("/api", methods = ['GET'])
def api1():
    return render_template("show.html", ins="Checking Sample API")

if __name__ == '__main__':
    app.run(debug=True)











    
 