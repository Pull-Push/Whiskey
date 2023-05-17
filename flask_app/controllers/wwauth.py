import os
from flask_app import app;
from flask import Flask, jsonify, render_template, request, abort
from flask_app.models.ww import WW
from pprint import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials
credential = ServiceAccountCredentials.from_json_keyfile_name("./creds.json",["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"])

client = gspread.authorize(credential)
gsheet = client.open("WW")

@app.route('/ww/', methods=["GET"])
def all_reviews():
    # print(gsheet.values_batch_get(["Year 1","Year 2","Year 3","Year 4","Year 5","Year 6","Year 7","Year 8"]).get("valueRanges"))
    # # print(gsheet.values_get("Year 1").get("values"))
        data = {
        "Year1": gsheet.values_get("Year 1").get("values"),
    #     "Year2": gsheet.values_get("Year 2").get("values"),
    #     "Year3": gsheet.values_get("Year 3").get("values"),
    #     "Year4": gsheet.values_get("Year 4").get("values"),
    #     "Year5": gsheet.values_get("Year 5").get("values"),
    #     "Year6": gsheet.values_get("Year 6").get("values"),
    #     "Year7": gsheet.values_get("Year 7").get("values"),
    #     "Year8": gsheet.values_get("Year 8").get("values")
    }
        pprint(data)
        return data;