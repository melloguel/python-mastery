import collections.abc
import csv

class RideData(collections.abc.Sequence):
    def __init__(self):
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        return len(self.routes)

    def __getitem__(self, index):
        return {
            'route' : self.routes[index],
            'date'  : self.dates[index],
            'daytype' : self.daytypes[index],
            'rides' : self.numrides[index],
        }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['ride'])

def read_rides_as_dicts(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            record = {
                'route' : row[0],
                'date' : row[1],
                'daytype' : row[2],
                'ride' : int(row[3]),
            }
            records.append(record)
    return records