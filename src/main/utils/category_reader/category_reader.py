import csv

def read_category(filename):
    keyword_category_map = {}
    with open(filename, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)  #remove header
        for row in csv_reader:
            try:
                key = row[0].strip().lower()
                category = row[1].strip().lower()
                subcategory = row[2].strip().lower()
                keyword_category_map[key] = {"category": category, "subcategory": subcategory}
            except:
                continue
    return keyword_category_map



