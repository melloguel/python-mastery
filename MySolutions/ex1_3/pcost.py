import sys

def cost(fname):
    total = 0
    with open(fname, 'r') as f:
        for line in f:
            stock, shares, price = line.split()
            total += int(shares) * int(price[:-1])
    return total

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemError("Usage: pcost.py filename")
    print(cost(sys.argv[1]))
