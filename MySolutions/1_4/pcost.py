def portfolio_cost(fname):
    total = 0
    with open(fname, 'r') as f:
        for line in f:
            cols = line.split()
            try:
                nshare = int(cols[1])
                price = float(cols[2])
                total += nshare * price
            except ValueError as e:
                print("Couldn't parse:", repr(line))
                print("Reason:", e)
    return total

if __name__ == "__main__":
    print(portfolio_cost('Data/portfolio2.dat'))