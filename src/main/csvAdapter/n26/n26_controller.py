import csv

from src.utils.const import DEFAULT_CURRENCY
from .classes import N26Entry
from src.main.csvAdapter.common import NewEntry

def read_from_csv(filename):
    entries = []
    with open(filename, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader) #remove header
        for row in csv_reader:
            entry = N26Entry(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
            entries.append(entry)
    return entries

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