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
        portfolio+= []
        
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
        
        
calculate_profit_loss("../../python_learning/Basic/Data/portfolio.csv")