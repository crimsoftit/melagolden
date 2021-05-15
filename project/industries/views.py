from flask import Flask, redirect, render_template, url_for, Blueprint
import os
from project import app

industries_blueprint = Blueprint('industries', __name__, template_folder='templates')

@industries_blueprint.route("/industries/fashion", methods=['GET'])
def fashion():
    return render_template('fashion.html')

@industries_blueprint.route("/industries/real_estate", methods=['GET'])
def real_estate():
    return render_template('real_estate.html')

@industries_blueprint.route("/industries/cpa", methods=['GET'])
def cpa():
    return render_template('cpa.html')
