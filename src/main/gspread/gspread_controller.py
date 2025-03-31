from .gspread_utils import *

def writeOnSpreadsheet(credentials_file, sheet_name, worksheet_name, data, intestation):
    sheet = getSpreadsheet(credentials_file, sheet_name)
    worksheet = selectWorksheet(sheet, worksheet_name)
    writeRow(worksheet, [intestation])
    for row in data:
        writeRow(worksheet, [row.date, row.beneficiary, row.currency, row.amount_eur, row.category, row.subcategory])