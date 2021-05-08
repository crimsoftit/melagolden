from flask import Flask, redirect, render_template, url_for
import os

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/company_profile', methods=['GET'])
def company_profile():
    return render_template('company_profile.html')

@app.route('/about/faqs', methods=['GET'])
def faq():
    return render_template('faq.html')

@app.route('/about/team', methods=['GET'])
def team():
    return render_template('team.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/about/how_it_works', methods=['GET'])
def how_it_works():
    return render_template('how_it_works.html')


if __name__ == '__main__':
    app.run()