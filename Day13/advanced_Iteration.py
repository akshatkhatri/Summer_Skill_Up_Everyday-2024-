import csv
from pprint import pprint
from collections import defaultdict
from readPortfolio import read_portfolio
'''
with open('portfolio.csv', newline='') as csvfile:
    readfile = csv.reader(csvfile)
    headers = next(readfile)
    byname = defaultdict(list)
    
    rows = list(readfile)

    for name,*data in rows:
        byname[name].append(data)
    
    for shares,prices in byname["IBM"]:
        print(shares,prices)
        
    for sno,(names,shares,prices) in enumerate(rows):
        print(sno, name, shares, prices)
        
    
    for row in rows:
        record = dict(zip(headers,row))
        print(record)
 '''
 
portfolio = read_portfolio('portfolio.csv')

print(sum(s["shares"] * s["prices"] for s in portfolio))

print(min(s["shares"] for s in portfolio))

print(any(s["name"] == "IBM" for s in portfolio)) 