class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
    
    def sell(self, nshares):
        if self.shares >= nshares:
            self.shares -= nshares
        else:
            raise ValueError(f"not enough shares to sell. Asked {nshares}, but have {self.shares}")
    
import csv

# A function that reads a file into a list of stocks
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            stock = Stock(row[0], int(row[1]), float(row[2]))
            portfolio.append(stock)
    return portfolio

def print_portfolio(portfolio):
    print('%10s %10s %12s'% ("name", "shares", "price"))
    print('{s:-^10} {s:-^10} {s:-^12}'.format(s=''))
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    print_portfolio(portfolio)
