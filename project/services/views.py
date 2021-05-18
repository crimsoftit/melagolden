from flask import Flask, redirect, render_template, url_for, Blueprint
import os
from project import app

services_blueprint = Blueprint('services', __name__, template_folder='templates')

@services_blueprint.route("/services/quickbooks_accounting_services/", methods=['GET'])
def quickbooks_accounting_services():
    return render_template('quickbooks_as.html')

@services_blueprint.route("/services/quickbooks_bookkeeping_services/", methods=['GET'])
def quickbooks_bookkeeping_services():
    return render_template('quickbooks_bs.html')

@services_blueprint.route("/services/accounts_receivable_services/", methods=['GET'])
def accounts_receivable_services():
    return render_template('accounts_receivable_ms.html')

@services_blueprint.route("/services/accounts_payable_services/", methods=['GET'])
def accounts_payable_services():
    return render_template('accounts_payable_services.html')

@services_blueprint.route("/services/payroll_services/", methods=['GET'])
def payroll_services():
    return render_template('payroll_services.html')

@services_blueprint.route("/services/tax_return_preperation_services/", methods=['GET'])
def tax_return_prep_services():
    return render_template('tax_prep.html')