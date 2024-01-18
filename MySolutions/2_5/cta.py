import sys
from collections import Counter, defaultdict
from pprint import pprint
from readrides import read_rides_as_dicts
import tracemalloc
if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemError("python cta.py <filename>")

    tracemalloc.start()
    rides = read_rides_as_dicts(sys.argv[1])

    print('1. How many bus routes exist in Chicago?')
    bus_rides_by_year = set((r['route'] for r in rides))
    print(len(bus_rides_by_year))

    print('2. How many people rode the number 22 bus on February 2, 2011?')
    total22 = sum((r['rides'] for r in rides
                    if r['route'] == '22' and r['date'] == '02/02/2011'))
    print(total22)
    # print('2.x What about any route on any date of your choosing?')      
    # total_any_route_any_date = Counter()
    # for r in rides:
    #     total_any_route_any_date[r.route, r.date] += r.rides
    # pprint(total_any_route_any_date)

    print('3. What is the total number of rides taken on each bus route?')
    total_rides_by_route = Counter() 
    for r in rides:
        total_rides_by_route[r['route']] += r['rides']
    
    for route, cnt in total_rides_by_route.most_common():
        print('%10s %10d' % (route, cnt))

    print('4. What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?')
    bus_rides_by_year = defaultdict(Counter)
    for r in rides:
        year = int(r['date'][-4:])
        bus_rides_by_year[year][r['route']] += r['rides']

    increase = bus_rides_by_year[2011] - bus_rides_by_year[2001]
    for r, inc in increase.most_common(5):
        print(r, inc) 

    curr, peak = tracemalloc.get_traced_memory()
    print(f"Memory usage: curr={curr/2**20:3.4f} Mb peak={peak/2**20:3.4f} Mb")