from flask import Flask, redirect, render_template, url_for, Blueprint
from project import app

about_blueprint = Blueprint('about', __name__, template_folder='templates')

@about_blueprint.route('/about/company_profile', methods=['GET'])
def company_profile():
    return render_template('company_profile.html')

@about_blueprint.route('/about/faqs', methods=['GET'])
def faq():
    return render_template('faq.html')

@about_blueprint.route('/about/team', methods=['GET'])
def team():
    return render_template('team.html')

@about_blueprint.route('/about/how_it_works', methods=['GET'])
def how_it_works():
    return render_template('how_it_works.html')