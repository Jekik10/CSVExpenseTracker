import csv

from src.utils.const import DEFAULT_CURRENCY
from .classes import RevolutEntry
from src.main.csvAdapter.common import NewEntry

def read_from_csv(filename):
    entries = []
    with open(filename, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader) #remove header
        for row in csv_reader:
            entry = RevolutEntry(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            entries.append(entry)
    return entries

def filter_columns(entries):
    new = []
    for entry in entries:
        if entry.state == "PENDING": #filtering pending entries
            continue
        ne = NewEntry(entry.started_date, entry.description, entry.currency, entry.amount)
        new.append(ne)
    return new