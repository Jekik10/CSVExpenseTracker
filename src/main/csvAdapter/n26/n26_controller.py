import csv

from src.utils.const import DEFAULT_CURRENCY
from .classes import Entry, NewEntry

def read_from_csv(filename):
    entries = []
    with open(filename, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader) #remove header
        for row in csv_reader:
            entry = Entry(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
            entries.append(entry)
    return entries

def remove_entry_by_keyword(entries, keyword):
    keyword = keyword.lower()
    correct_entries = []
    for entry in entries:
        if keyword in entry.beneficiary.lower():
            continue
        else:
            correct_entries.append(entry)
    return correct_entries

def edit_transfers(entries):
    correct_entries = []
    for entry in entries: 
        if "transfer" in entry.transaction_type.lower():
            entry.beneficiary = entry.beneficiary + ": " + entry.payment_reference
            entry.currency = DEFAULT_CURRENCY
        correct_entries.append(entry)
    return correct_entries

def filter_columns(entries):
    new = []
    for entry in entries:
        ne = NewEntry(entry.value_date, entry.beneficiary, entry.currency, entry.amount_eur)
        new.append(ne)
    return new

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
