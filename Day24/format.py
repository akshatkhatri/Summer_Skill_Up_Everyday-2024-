# name = 'IBM'
# shares = 100
# price = 91.1

# print(f"{name:>10s} {shares:>10d} {price:>10.2f}")

# s = {
#     'name' : 'IBM',
#     'shares' : 100,
#     'price' : 91.1
# }

# '{name:>10s} {shares:10d} {price:10.2f}'.format_map(s)



import csv

filename = "../../python_learning/Basic/Data/portfolio.csv"

def read_portfolio_as_tuple(filename):
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

def read_portfolio_as_dict(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = []
        for row in rows:
            t = {}
            t['share_name'] = row[0]
            t['share_quant'] = int(row[1])
            t['share_price'] = float(row[2])   
            portfolio.append(t)
    return portfolio

def read_prices(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        t = {}
        for row in rows:
            # if(row != []):
                
                t[row[0]] = float(row[1])   
    return t    

def calculate_profit_loss(portfolio):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        actual_prices = read_prices("../../python_learning/Basic/Data/prices.csv")
        headers = next(rows)
        total = 0
        index = 1
        for row in rows:
            total += (actual_prices[row[0]]- float(row[2]))*int(row[1])
            print(f"Your total balance on day {index} is {total}")
            index += 1
            
        if(total >= 0):
            print(f"Congratulations ! you made a profit of {total}")
        
        else:
            print(f"Sad you made a loss of {total}")
        
        
# calculate_profit_loss("../../python_learning/Basic/Data/portfolio.csv")

def make_report(portfolio,market_prices):
    my_portfolio = read_portfolio_as_dict(portfolio)
    actual_prices = read_prices(market_prices)

    print(f'{"name":>15s} {"Shares":>15s} {"Price":>15s} {"Share_Price":>15s} {"Market_price":>15s} {"Profit/Loss made":>15s}',end = "\n\n")
    print("---------------------------------------------------------------------------------------------------------")
    for t in my_portfolio:
        market_price = actual_prices[t['share_name']]
        stock_change = market_price - t['share_price']
        print(f"{t['share_name']:>15s} {t['share_quant']:15d} ${t['share_price']:15.2f} ${market_price :>15.2f} ${stock_change:>15.2f}")
        
        
    
    