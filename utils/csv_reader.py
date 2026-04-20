import csv

def get_csv_data(filename):
    rows = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader, None)
        for row in reader:
            rows.append(row)
        return rows