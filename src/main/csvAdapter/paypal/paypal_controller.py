import csv
from .classes import *
# from src.utils.const import DEFAULT_CURRENCY

def read_from_csv(filename):
    with open(filename) as csv_file:
        data = csv.DictReader(csv_file, delimiter=",")
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

def remove_entry_by_keyword(entries, keyword):
    keyword = keyword.lower()
    correct_entries = []
    for entry in entries:
        if keyword in entry.beneficiary.lower():
            continue
        else:
            correct_entries.append(entry)
    return correct_entries

def set_category(entries, keyword_category_map):
    for entry in entries:
        for keyword in keyword_category_map:
            if keyword in entry.beneficiary.lower():
                entry.category = keyword_category_map[keyword]["category"]
                entry.subcategory = keyword_category_map[keyword]["subcategory"]
    return entries

def create_output_file(entries, output_filename):
    with open(output_filename, "w", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=";")
        for entry in entries:
            csv_writer.writerow([entry.date, entry.beneficiary, entry.currency, entry.amount_eur, entry.category, entry.subcategory])
    print("done write on "+ output_filename)
