from flask import Flask, redirect, render_template, url_for, Blueprint
import os
from project import app

home_blueprint = Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/')
def index():
    return render_template('index.html')

@home_blueprint.route('/contact/', methods=['GET'])
def contact():
    return render_template('contact.html')