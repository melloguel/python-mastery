import sys

def cost(fname):
    total = 0
    with open(fname, 'r') as f:
        for line in f:
            cols = line.split()
            nshare = int(cols[1])
            price = float(cols[2])
            total += nshare * price
    return total

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemError("usage: pcost.py filename")
    print(cost(sys.argv[1]))