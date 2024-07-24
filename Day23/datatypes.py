import csv

filename = "../../python_learning/Basic/Data/portfolio.csv"

def read_portfolio(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = []
        
        for row in rows:
            share_name = row[0]
            share_quant = int(row[1])
            share_price = float(row[2])
            t = (share_name,share_quant,share_price)
            portfolio.append(t)
    return portfolio    