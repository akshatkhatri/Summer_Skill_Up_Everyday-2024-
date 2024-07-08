import re

email = input("Please Enter Your Email").strip()

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$",email):
#     print("Valid")

# else:
#     print("invalid")

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|net)$",email,re.IGNORECASE): #/w means word character it includes [a-zA-Z0-9_]
    print("Valid")

else:
    print("invalid")