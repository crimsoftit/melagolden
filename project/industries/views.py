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

@industries_blueprint.route("/industries/retail_store/", methods=['GET'])
def retail_store():
    return render_template('retail_store.html')

@industries_blueprint.route("/industries/travel_agency/", methods=['GET'])
def travel_agency():
    return render_template('travel_agency.html')

@industries_blueprint.route("/industries/cpa/", methods=['GET'])
def cpa():
    return render_template('cpa.html')

@industries_blueprint.route("/industries/startups/", methods=['GET'])
def startups():
    return render_template('startups.html')

@industries_blueprint.route("/industries/restaurants/", methods=['GET'])
def restaurants():
    return render_template('restaurants.html')

@industries_blueprint.route("/industries/manufacturing/", methods=['GET'])
def manufacturing():
    return render_template('manufacturing.html')

@industries_blueprint.route("/industries/amazon_sellers/", methods=['GET'])
def amazon_sellers():
    return render_template('amazon_sellers.html')
