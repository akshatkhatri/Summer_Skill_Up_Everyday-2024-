# 1st way

# i=0
# while i<3:
#     print("loop executing")
#     i+=1

# 2nd way

# for i in [0,1,2]:
#     print("loop2 executing")

# 3rd way

# for i in range(3):
#     print("Loop executing")

# 4th way

# for _ in range(3):
#     print("Loop executing")

# 5th way

# print("meow\n" * 3, end="")

# 6th way

def main():
    while True:
        n=int(input("Please Enter A Value of N for meowing"))

        if n>0:
            break

    meow(n)

def meow(n):
    for _ in range(n):
        print("Meow\n",end="")

main()