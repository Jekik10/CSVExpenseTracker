import csv

def read_blacklist(filename):
    blacklist = []
    with open(filename, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)  #remove header
        for row in csv_reader:
            try:
                word = row[0].strip().lower()
                blacklist.append(word)
            except:
                continue
    return blacklist



