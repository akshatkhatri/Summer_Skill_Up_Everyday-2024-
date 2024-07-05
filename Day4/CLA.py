import sys

# try:
#     print("hello, my name is ",sys.argv[1])

# except IndexError:
#     print("incorrect number of arguments")
    
# if(len(sys.argv)<2):
#     print("Too Few Arguments")

# elif(len(sys.argv)>2):
#     print("Too many arguments")

# else:
#     print("hello, my name is ",sys.argv[1])

# for arg in sys.argv:
#     print(arg)

# if(len(sys.argv)<2):
#     sys.exit("Too Few Arguments")

# elif(len(sys.argv)>2):
#     sys.exit("Too many arguments")


# print("hello, my name is ",sys.argv[1])

for arg in sys.argv[1:]:
    print(arg)

if(len(sys.argv)<2):
    sys.exit("Too Few Arguments")

elif(len(sys.argv)>2):
    sys.exit("Too many arguments")


print("hello, my name is ",sys.argv[1])