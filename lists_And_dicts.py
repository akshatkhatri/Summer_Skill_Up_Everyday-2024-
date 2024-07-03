# students={"Akshat": "Sec-23",
#           "Ishita":"Sonipat",
#           "Ally":"626",
# }

# print(students["Akshat"])

# for student in students:
#     print(student,students[student],sep="-> ")

students=[{"name":"Akshat","Address":"Sec-23","color":"Green"},
          {"name":"Ishita","Address":"626","color":"Pink"},
          {"name":"Anshul","Address":"Near raju palace","color":"Red"},
          {"name":"Ally","Address":"626 sec 23","color":None},
]

for student in students:
    print(student["name"],student["Address"],student["color"],sep=", ")

    