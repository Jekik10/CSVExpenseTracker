import csv
from src.main.csvAdapter.common import *
# from src.utils.const import DEFAULT_CURRENCY

def read_from_csv(filename):
    with open(filename) as csv_file:
        data = csv.DictReader(csv_file, delimiter=",")
        data.fieldnames = [row.replace('ï»¿', '') for row in data.fieldnames]
        data.fieldnames = [row.replace('\ufeff', '') for row in data.fieldnames]
        data.fieldnames = [row.replace('"', '') for row in data.fieldnames]
        return list(data)
    
def filter_columns(entries):
    new = []
    for entry in entries:
        if entry["Nome"] == "PayPal": # prepayment/requests
            continue
        if entry["Stato"] == "Completata" : # consider just completed
            ne = NewEntry(entry["Data"], entry["Nome"]+": "+entry["Messaggio"], entry["Valuta"], str(entry["Netto"]).replace(",", "."))
            new.append(ne)
    return new