# Python ex 1_3.md
import sys

def portfolio_cost(filename):
    total_stock_cost = 0
    with open(filename,"r") as file:
        data = file.readlines()

        for line in data:
            stock_info = line.split()

            try:
                if len(stock_info) != 3:
                    raise RuntimeError
            except RuntimeError:
                print("Incomplete Data on Line with values")
                sys.exit(line)

            
            stock_name =  stock_info[0]
            try:
                stock_quant = int(stock_info[1])
                stock_price = float(stock_info[2])
            except ValueError:
                print("Stock Price and Quantity can only be integers")
                print(line)
                

            total_stock_cost += stock_quant * stock_price
    return total_stock_cost

try:
    print(portfolio_cost("portfolio2.dat"))
except FileNotFoundError:
    print("FIle was not found or had an invalid location".upper())