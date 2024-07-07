# import sys

# name = sys.argv[1]

# fileVar = open("names.txt", "a")

# fileVar.write(f"{name}\n")

# fileVar.close()


# with open("names.txt","r") as file:
#     lines = file.readlines()

# for line in lines :
#     print("Hello,",line,end="")

# with open("names.txt","r") as file:
#     for line in file :
#         print(line,end = "")

names= []

with open("names.txt","r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names,reverse=False):
    print(f"Hello, {name}")