import re
# https://www.linkedin.com/in/akshat-khatri-c/

url = input("What's your Linkedin URL").strip()

if matches := re.search(r"^https?://(www\.)?linkedin.com/in/([^/]+)/?$",url,re.IGNORECASE):
    print(matches[2])

else:
    print("not valid")

