from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to create a database connection
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()

    if user and user['password'] == password:
        return f'Logged in as {username} (Email: {user["email"]})'
    else:
        return 'Invalid credentials. Please try again.'

@app.route("/api", methods=['GET'])
def api1():
    return render_template("show.html", ins="Checking Sample API")

if __name__ == '__main__':
    app.run(debug=True)











    
 