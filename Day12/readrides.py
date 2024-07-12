import tracemalloc
import csv 
class Readrides:

    def __init__(self, file):
        self.file = file

    def Reading_Csv_As_A_String(self):
        with open(self.file, "r") as file:
            tracemalloc.start()
            data = file.read()

            current, peak = tracemalloc.get_traced_memory()
            print(f"Current memory used is {current} and peak {peak}")

    def Reading_Csv_As_A_ListOfStrings(self):
        with open(self.file, "r") as file:
            tracemalloc.start()
            lines = file.readlines()

            current, peak = tracemalloc.get_traced_memory()
            print(f"Current memory used is {current} and peak {peak}")

    def Reading_Csv_As_A_ListOfTuples(self):
            records = []
            with open(self.file, "r") as file:
                rows = csv.reader(file)
                headings = next(rows)
                for row in rows :
                    route = row[0]
                    date = row[1]
                    day = row[2]
                    rides = int(row[3])

                    record = (route, date, day, rides)
                    records.append(record)
            return records

    def read_rides_as_dicts(self):
        Bus_data = []
        with open(self.file) as file:
            rows = csv.reader(file)
            headers = next(rows)

            for row in rows:
                records ={
                    "route" : row[0],
                    "date" : row[1],
                    "daytype" : row[2],
                    "rides" : int(row[3])
                }
                Bus_data.append(records)
            
            return Bus_data



                

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()

    RideFile = Readrides("ctabus.csv")
    Tuple_records = Readrides.read_rides_as_dicts(RideFile)
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())