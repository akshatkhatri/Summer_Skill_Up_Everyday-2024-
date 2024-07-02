name=input("what's your name ")
name=name.strip()
name=name.title()

firstname,lastname=name.split(" ")
print("my name is",name,sep="-")

# giving a format string using the 'f' specifier
print(f"my first name is {firstname} and my last name is {lastname}")