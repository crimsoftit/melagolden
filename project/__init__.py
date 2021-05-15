from flask import Flask, redirect, render_template, url_for
import os

app = Flask(__name__)


from project.home.views import home_blueprint
from project.about.views import about_blueprint
from project.services.views import services_blueprint
from project.industries.views import industries_blueprint


app.register_blueprint(home_blueprint)
app.register_blueprint(about_blueprint)
app.register_blueprint(services_blueprint)
app.register_blueprint(industries_blueprint)













