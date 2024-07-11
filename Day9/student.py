import re

def main():
    email = input("What's your email? ")

    student = get_details()
    print(f"{student[0]} lives in {student[1]}")
    

def get_details():
    name = input("What's student's name? ")
    house = input("what's your house? ")

    return (name,house)
    
if __name__ == "__main__":
    main()

    