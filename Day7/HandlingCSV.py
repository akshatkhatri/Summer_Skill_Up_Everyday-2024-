CustomerData = []

with open("customer.csv","r") as datafile:
    for line in datafile:
         sno,Fname,Lname,email,date,sub = line.rstrip().split(",")
         customerDict={"sno":sno,"Fname":Fname,"Lname":Lname,
                       "email":email,"date":date,"sub":sub}
         
         CustomerData.append(customerDict)

def get_name(customer):
     return f"{customer['Fname']} + ' ' + {customer['Lname']}"

def customerdict_to_csv(customer):
     return f'{customer["sno"]},{customer["Fname"]},{customer["Lname"]},{customer["email"]},{customer["date"]},{customer["sub"]}\n'
     
with open("updatedCustomerFile.csv","w") as newdatafile:
    for customer in sorted(CustomerData,key = get_name):
         newdatafile.write(customerdict_to_csv(customer))
     