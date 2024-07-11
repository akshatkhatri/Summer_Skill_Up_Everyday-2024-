class Wizard:
        def __init__(self, name):
            if not name:
                raise ValueError("Name should be a non empty Value")
            
            self._name = name


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name) #Class Inheritance
        self._house = house
    
    def __str__(self):
        print(f"The student's name is {self._name} and lives in {self._house}")
        
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self._subject = subject

student = Student("Akshat","Sector-23")
professor = Professor("Prof woof woof","Python Programming")
wizard = Wizard("Albalus")

print(professor._name,student._name,sep = "\n")
