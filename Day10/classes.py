import random

class Student :
    def __init__(self, name, age, grade):

        self._name = name
        self.age = age
        self._grade = grade 

    def __str__(self):
        return f"{self._name} is {self._age} years old and is in grade {self._grade}"

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Empty Name Can't be treated")
        
        self._name = name
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age>25:
            raise ValueError("Age is required / Greater than 25")

        self._age = age
    
    @property
    def grade(self):
        return self.grade
    
    @grade.setter
    def grade(self,grade):
        if not grade:
            raise ValueError("Invalid Grade")
        
        self._grade = grade

class Home:
    names=["Akshat","Ishita","Anshul","Ally"]

    @classmethod
    def random_name(cls,designation):
        print(f"{random.choice(cls.names)} is a {designation}")

    @classmethod
    def get_designation(cls):
        desig = input("What do you want to call? ")
        return desig

def main():
    Home.random_name(Home.get_designation())
    student = get_student()
    print(student)

def get_student():
    name = input("What's student's name? ")
    age = int(input("What's student's age? "))
    grade = input("What's student's grade? ")
    return Student(name, age, grade)    
  

if __name__ == "__main__":
    main()


