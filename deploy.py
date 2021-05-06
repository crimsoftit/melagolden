from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)
app.config.from_object('config.BaseConfig')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/company_profile', methods=['GET'])
def company_profile():
    return render_template('company_profile.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()