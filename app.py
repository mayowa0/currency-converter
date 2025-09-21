from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "fallbacksecret")  # Needed for sessions

API_KEY = os.environ.get("API_KEY")  # Store API key in environment, not code

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        if not username or not password:
            return "<h1>Username and password cannot be empty</h1><a href='/signup'>Try again</a>"

        hashed_password = generate_password_hash(password)

        with open('users.txt', 'a') as file:
            file.write(f"{username},{hashed_password}\n")

        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        if not os.path.exists('users.txt'):
            return "<h1>No users found. Please sign up first.</h1><br><a href='/signup'>Sign Up</a>"

        with open('users.txt', 'r') as file:
            for line in file:
                stored_user, stored_pass = line.strip().split(',')
                if stored_user == username and check_password_hash(stored_pass, password):
                    session['username'] = username
                    return redirect(url_for('convert'))

        return "<h1>Invalid credentials</h1><br><a href='/login'>Try again</a>"

    return render_template('login.html')

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    if 'username' not in session:
        return redirect(url_for('login'))

    currency_list = ['USD', 'NGN', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'ZAR', 'KES', 'GHS']
    result = None
    from_currency = to_currency = amount = ''

    if request.method == 'POST':
        try:
            from_currency = request.form['from_currency']
            to_currency = request.form['to_currency']
            amount = float(request.form['amount'])

            url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_currency}/{to_currency}/{amount}"
            response = requests.get(url)
            data = response.json()

            if data.get('result') == 'success':
                result = data['conversion_result']
            else:
                result = f"Error: {data.get('error-type', 'Unknown error')}"

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template(
        'convert.html',
        result=result,
        currency_list=currency_list,
        from_currency=from_currency,
        to_currency=to_currency,
        amount=amount
    )

if __name__ == '__main__':
    app.run(debug=True)

