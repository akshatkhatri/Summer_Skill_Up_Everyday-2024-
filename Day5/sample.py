import sys

def main():

    if(len(sys.argv))<2:
        sys.exit("Too few args")
        
    hello(sys.argv[1])
    goodbye(sys.argv[1])

def hello(pname):
    print(f"hello {pname}")

def goodbye(pname):
    print(f"goodbye {pname}")

if __name__=="__main__": # This line checks if the file the function is being called from is not something other than main
    main()