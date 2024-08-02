a = [1,2,3,4,5]

b = [x ** 5 for x in a]

print(b)

names = ["ELwood","JPLER"]

update_names = [name.lower() for name in names]
print(update_names)

# we can also filter in a list 

a = [1,-5,4,2,-2,10]

b = [x ** 3 for x in a if x > 0]

print(b)