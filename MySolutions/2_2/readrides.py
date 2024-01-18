from collections import namedtuple
import csv

def _tuple(route, date, daytype, rides):
    return (route, date, daytype, rides)

def _dictionary(route, date, daytype, rides):
    row = {
        'route': route,
        'date': date,
        'daytype': daytype,
        'rides': rides,
    }
    return row

class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def _Row(route, date, daytype, rides):
    return Row(route, date, daytype, rides)

NamedTupleRow = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])
def _namedtuple(route, date, daytype, rides):
    return NamedTupleRow(route, date, daytype, rides)

class SlotRow:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides
    
    def __repr__(self):
        return f"SlotRow({self.route!r}, {self.date!r}, {self.daytype!r}, {self.rides!r})"

def _SlotRow(route, date, daytype, rides):
    return SlotRow(route, date, daytype, rides)

def read_rides_as(filename, creator):
    '''
    Read the bus ride data as a list of objects
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = creator(route, date, daytype, rides)
            records.append(record)
    return records

def trace_function(f, *args):
    tracemalloc.start()
    out = f(*args)
    curr, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return curr, peak

if __name__ == '__main__':
    import tracemalloc

    methods = {
        'tuple' : _tuple,
        'dictionary' : _dictionary,
        'class' : _Row,
        'named tuple' : _namedtuple,
        'SlotRow': _SlotRow,
    }

    # tracemalloc.start()
    # rows = read_rides_as('Data/ctabus.csv', lambda a, b, c, d: (a, b, c, d))
    # print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    results = []
    for method, f in methods.items():
        result = trace_function(read_rides_as, 'Data/ctabus.csv', f)
        results.append((result, method))

    print('position\t      method\t    last\t    peak') 
    for i, ((curr, peak), method) in enumerate(sorted(results), 1):
        s = '%8s\t%12s\t%3.2fMB\t%3.2fMB' % (str(i), method, curr / 2**20, peak/2**20)
        print(s)
    
