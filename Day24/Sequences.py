# names = ["Akshat","Ishita","Anshul"]

# for i,name in enumerate(names,start = 1):
#     print(i,name)
    
# points = [
# (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
# ]
# for x, y in points:
#     print(x,y)
    
# columns = ['name','shares','price']
# values = ['IBM',100,91.1]

# pairs = zip(columns,values)

# for column,value in pairs:
#     print(column,value)
    
# # A common use case for zip is to construct dictionaries using key-value pairs

# d = dict(pairs)
# print(d)
import csv

def read_portfolio_as_dict(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = []
        for rowno,row in enumerate(rows):
            try:
                t = {}
                t['share_name'] = row[0]
                t['share_quant'] = int(row[1])
                t['share_price'] = float(row[2])   
                portfolio.append(t)
                
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')    
    return portfolio


