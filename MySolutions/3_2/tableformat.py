def print_table(lob, loa):
    print(' '.join(f'{a: >12}' for a in loa))
    print(' '.join('-'*12 for _ in loa))
    for o in lob:
        print(' '.join('%12s' % getattr(o, attr) for attr in loa ))

if __name__ == '__main__':
    import sys
    sys.path.append('MySolutions/3_1/')

    import stock
    portfolio = stock.read_portfolio('Data/portfolio.csv')
    print_table(portfolio, ['name', 'shares', 'price'])
    print()
    print_table(portfolio, ['shares', 'name'])