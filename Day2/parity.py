def main():
    x=int(input("the value of x "))

    if is_even(x):
        print("number is even")
    else:
        print("number is odd")

'''

1st way of defining function
def is_even(x):
    if x%2==0:
        return True
    else:
        return False
    

2nd way of defining function
def is_even(x):
    return True if x%2==0 else False


3rd way of defining fucntion

'''

def is_even(x):
    return x%2==0

main() #Function call for program execution