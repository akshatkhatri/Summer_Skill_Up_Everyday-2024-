import csv
from collections import Counter
from collections import defaultdict
portfolio = []
def read_portfolio(filename):
    with open(filename,"r") as file:
        rows = csv.reader(file)
        headers = next(rows)

        for row in rows :
            record ={
                "name" : row[0],
                "shares" : int(row[1]),
                "prices" : float(row[2])
            }

            portfolio.append(record)
        return portfolio
def main():   
    portfolio = read_portfolio("portfolio.csv")

    low_price_stocks = [s for s in portfolio if s["prices"] <= 52]
    print(low_price_stocks)

    Total_Portfolio_cost = sum([s["shares"] * s["prices"] for s in portfolio])
    print(Total_Portfolio_cost)

    All_stocks = {s["name"] for s in portfolio}
    print(All_stocks)


    Total_stock_holding = {s["name"] : 0 for s in portfolio}

    for s in portfolio:
        Total_stock_holding[s["name"]] += s["shares"]

        print(f"\n{Total_stock_holding}")

    totals = Counter()

    for s in portfolio:
        totals[s["name"]] += s["shares"]

    All_stocks_info = defaultdict(list)

    for s in portfolio:
        All_stocks_info[s["name"]].append(s) 
        
        
if __name__ == "__main__":
    main()