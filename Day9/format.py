# a program to interpret khatri, akshat the same as akshat khatri
#using regex
import re

name = input("what's your name? ")

# matches = re.search("^([a-zA-z]+), ?([a-zA-z]+)$",name)

# if matches:
#     last,first = matches.groups()
#     name = f"{first} {last}" # the regex will update first and last with the name variable

# print(f"Hello, {name}")

#instead of asking for if like in above statements , we can 

if matches := re.search("^([a-zA-z]+), ?([a-zA-z]+)$",name):
    last,first = matches.groups()
    name = f"{first} {last}" # the regex will update first and last with the name variable

print(f"Hello, {name}")

