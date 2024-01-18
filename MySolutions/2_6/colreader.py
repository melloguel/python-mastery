import collections.abc
import csv

class DataCollection(collections.abc.Sequence):
    __slots__ = ["cols", "cols_names", "byname"]
    def __init__(self, cols_names):
        self.cols = [[] for _ in cols_names]
        self.cols_names = list(cols_names)
        self.byname = { name : idx for idx, name in enumerate(cols_names)}
    
    def __repr__(self):
        return f"DataClass({self.cols_names!r})"

    def __len__(self):
        return len(self.cols[0])

    def __getitem__(self, idx):
        return dict(zip(self.cols_names, (c[idx] for c in self.cols)))

    def append(self, d):
        for k, v in d.items():
            self.cols[self.byname[k]].append(v)


def read_csv_as_columns(fname, col_type):
    with open(fname, 'r') as f:
        f_csv = csv.reader(f)
        header = next(f_csv)
        records = DataCollection(header)
        for row in f_csv:
            records.append(dict(zip(header, (f(r) for f, r in zip(col_type, row)))))
        return records