from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


user_data = []

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        
        username = request.form.get('username')
        password = request.form.get('password')

        
        user_data.append({"username": username, "password": password})

        
        return redirect(url_for('login'))

    return render_template('sign.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == 'main':
    app.run(debug=True)