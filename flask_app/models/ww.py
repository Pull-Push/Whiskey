import gspread
from oauth2client.service_account import ServiceAccountCredentials
credential = ServiceAccountCredentials.from_json_keyfile_name("./creds.json",["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"])
import json


client = gspread.authorize(credential)
gsheet = client.open("WW")




class WW:
    def __init__(self, data) -> None:
        pass


    @classmethod
    def get_all(cls):
        # allWW = {
        #     "Year1": gsheet.values_get("Year 1").get("values"),
        #     "Year2": gsheet.values_get("Year 2").get("values"),
        #     "Year3": gsheet.values_get("Year 3").get("values"),
        #     "Year4": gsheet.values_get("Year 4").get("values"),
        #     "Year5": gsheet.values_get("Year 5").get("values"),
        #     "Year6": gsheet.values_get("Year 6").get("values"),
        #     "Year7": gsheet.values_get("Year 7").get("values"),
        #     "Year8": gsheet.values_get("Year 8").get("values")
        # }
        allWW = gsheet.values_get("WW").get("values")
        print(allWW)
        return allWW
