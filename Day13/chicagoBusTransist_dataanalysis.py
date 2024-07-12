import readrides
from collections import Counter
from collections import defaultdict
import re

def Total_Bus_routes_in_chicago():

    rows = readrides.read_rides_as_dicts("ctabus.csv")
    unique_routes = set(row["route"] for row in rows)
    num_routes = len(unique_routes)
    
    print(f"Total number of bus routes in Chicago: {num_routes}")
    

def Bus_rides_on_any_date(date):
    rows = readrides.read_rides_as_dicts("ctabus.csv")
    Bus_rides_on_date = [row["rides"] for row in rows if row["date"] == date]
    passengers_on_a_date = sum(Bus_rides_on_date)
    print(f"passengers on {date} is {passengers_on_a_date}")

def date_validation(date):
    if (matches := re.search(r"^[0-9]([0-9])+/([0-9])[0-9]+/(200[1-9]|201[0-3])$",date)):
        return True
    else:
        print("Invalid Date , put date in the format DD/MM/YEAR")
        return False

def Bus_rides_on_each_route():
    rows = readrides.read_rides_as_dicts("ctabus.csv")
    route_counts = Counter()
    for row in rows:
        route_counts[row["route"]] += 1  # Counting occurrences of each route
    
    print(route_counts)

def Bus_5_routes_with_the_greatest_increase_in_ridership():
    rides_data = readrides.read_rides_as_dicts("ctabus.csv")
    route_rides = defaultdict(lambda: {'rides_2001': 0, 'rides_2011': 0})
    
   
    for ride in rides_data:
        year = int(ride['date'].split('/')[2])  
        if year == 2001:
            route_rides[ride['route']]['rides_2001'] += int(ride['rides'])
        elif year == 2011:
            route_rides[ride['route']]['rides_2011'] += int(ride['rides'])
    
    
    route_increases = {}
    for route, rides in route_rides.items():
        increase = rides['rides_2011'] - rides['rides_2001']
        route_increases[route] = increase
    
    
    top_routes = sorted(route_increases.items(), key=lambda x: x[1], reverse=True)
    print(top_routes[:5])
        
def main():
    
    # Added regex for date validation 
    Total_Bus_routes_in_chicago()  
    
    date = input("please enter date") 
    if date_validation(date):
        Bus_rides_on_any_date(date)
        
    Bus_rides_on_each_route()
    Bus_5_routes_with_the_greatest_increase_in_ridership()
if __name__ == "__main__":
    main()