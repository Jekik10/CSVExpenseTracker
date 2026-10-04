import csv

from src.utils.const import DEFAULT_CURRENCY
from .classes import TradeRepublicEntry
from src.main.csvAdapter.common import NewEntry

def read_from_csv(filename):
    entries = []
    with open(filename, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader) #remove header
        for row in csv_reader:
            entry = TradeRepublicEntry(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22])
            entries.append(entry)
    return entries

def filter_columns(entries):
    new = []
    for entry in entries:
        if entry.type != "CARD_TRANSACTION":
            continue
        ne = NewEntry(entry.datetime, entry.description, entry.currency, entry.amount)
        new.append(ne)
    return new