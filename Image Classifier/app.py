from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/Login')  
def login():
    return render_template('Login.html')  

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':  
    app.run(debug=True)
