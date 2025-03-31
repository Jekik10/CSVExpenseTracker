import gspread
from google.oauth2.service_account import Credentials

def getSpreadsheet(credentials_file, sheet_name):
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(credentials_file, scopes=SCOPES)
    client = gspread.authorize(creds)

    spreadsheet = client.open(sheet_name)
    return spreadsheet


def selectWorksheet(spreadsheet, worksheet_name):
    return spreadsheet.worksheet(worksheet_name)

def writeCell(sheet, cell, content):
    sheet.update(cell, [[content]])

def readCell(sheet, cell):
    return sheet.acell(cell).value

def writeRow(sheet, row):
    sheet.append_row(row, value_input_option="USER_ENTERED")