class Stock:
    _types = (str, int, float)
    __slots__ = ("_name", "_shares", "_price")
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        t = self._types[0]
        if not isinstance(value, t):
            raise TypeError(f'Expected {t.__name__}, got {type(value).__name__}')
        self._name = value

    @property
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        t = self._types[1]
        if not isinstance(value, t):
            raise TypeError(f'Expected {t.__name__}, got {type(value).__name__}')
        if value < 0:
            raise ValueError(f'Expected non negative value, got {value}')
        self._shares = value
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        t = self._types[2]
        if not isinstance(value, t):
            raise TypeError(f'Expected {t.__name__}, got {type(value).__name__}')
        if value < 0:
            raise ValueError(f'Expected non negative value, got {value}')
        self._price = value

    def sell(self, nshares):
        self.shares -= nshares

from decimal import Decimal
class DStock(Stock):
    _types = (str, int, Decimal)

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

