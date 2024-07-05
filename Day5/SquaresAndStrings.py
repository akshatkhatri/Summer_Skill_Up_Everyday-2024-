def main():
    num=int(input("Enter the value for number"))
    square(num)
    name=input("what's your name? ")
    print(hello(name))


def square(num):
    return num*num

def hello(name="World"):
    return f"hello, {name}"

if __name__=="__main__":
    main()

