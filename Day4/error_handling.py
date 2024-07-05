def main():
    x=getInt()
    print(f"x is {x}")

def getInt():
    while True:
        try:
            x=int(input("WHat's X ?"))

        except ValueError:
            pass

        else:
            return x
            

main()