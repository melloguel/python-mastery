import csv

def read_csv_as_dicts(fname, col_types):
    records = []
    with open(fname, 'r') as f:
        f_csv = csv.reader(f)
        header = next(f_csv)
        for row in f_csv:
            records.append(dict(zip(header, (f(r) for f, r in zip(col_types, row)))))
        return records

