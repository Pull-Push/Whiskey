from flask_app import app
from flask import render_template, jsonify,request,abort;
from flask_app.controllers import users;
from flask_app.controllers import whiskies;
from flask_app.controllers import wwauth

import os

# Google Sheets API Setup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

@app.route("/")
def index():
    return render_template("index.html");


if __name__ == "__main__":
    app.run(debug=True)