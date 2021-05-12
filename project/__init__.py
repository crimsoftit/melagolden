from flask import Flask, redirect, render_template, url_for
import os

app = Flask(__name__)


from project.home.views import home_blueprint
from project.about.views import about_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(about_blueprint)




@app.route("/services/quickbooks_accounting_services", methods=['GET'])
def quickbooks_accounting_services():
    return render_template('quickbooks_as.html')

@app.route("/services/quickbooks_bookkeeping_services", methods=['GET'])
def quickbooks_bookkeeping_services():
    return render_template('quickbooks_bs.html')

@app.route("/services/accounts_receivable_services", methods=['GET'])
def accounts_receivable_services():
    return render_template('accounts_receivable_ms.html')



@app.route("/services/payroll_services", methods=['GET'])
def payroll_services():
    return render_template('payroll_services.html')

@app.route("/industries/cpa", methods=['GET'])
def cpa():
    return render_template('cpa.html')



