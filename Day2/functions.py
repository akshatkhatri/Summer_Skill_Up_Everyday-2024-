#function define of main
def main():
    hello()
    name=input("enter your name.")
    hello(name)

# function defination to hello function
def hello(to="world"):
    print("hello",to)
    print("thank you !!")

def favdigit(digit=2):
    fvdigit=input("enter your fav digit")
    return fvdigit

#function call to main()
main()