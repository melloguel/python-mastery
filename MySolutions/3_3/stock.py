class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def cost(self):
        return self.shares * self.price
    
    def sell(self, nshares):
        if self.shares >= nshares:
            self.shares -= nshares
        else:
            raise ValueError(f"not enough shares to sell. Asked {nshares}, but have {self.shares}")

from decimal import Decimal
class DStock(Stock):
    types = (str, int, Decimal)

def print_portfolio(portfolio):
    print('%10s %10s %12s'% ("name", "shares", "price"))
    print('{s:-^10} {s:-^10} {s:-^12}'.format(s=''))
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))


if __name__ == '__main__':
    import sys
    sys.path.append('MySolutions/3_3')
    from reader import read_csv_as_instances

    portfolio = read_csv_as_instances('Data/portfolio.csv', Stock)
    print_portfolio(portfolio)
    print(type(portfolio[0].price))

    print('\n'*4)

    dportfolio = read_csv_as_instances('Data/portfolio.csv', DStock)
    print_portfolio(dportfolio)
    print(type(dportfolio[0].price))

