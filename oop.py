class Movie:
    def __init__(self,title,rating):
        self.title=title
        self.rating=rating
    def display(self):
        print(f"Title:{self.title},Rating:{self.rating}")

m1=Movie("Kantara 1",10)
m2=Movie("Kantara 2",9)
m1.display()
m2.display()

class Mobile:
    def __init__(self,brand,prize):
        self.brand=brand
        self.prize=prize
    def display(self):
        print(f"Brand:{self.brand},Prize:{self.prize}")
mo1=Mobile("Vivo",30000)
mo2=Mobile("Realme",50000)
mo1.display()
mo2.display()


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_info(self):
        print(f"Name:{self.name},Marks:{self.marks}")    
s1=Student("Ansha",88)
s2=Student("Ganesh",91)
s1.display_info()
s2.display_info()

### Using Default Parameters
class Employee:
    def __init__(self,name,salary=30000):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"Name:{self.name},Salary:{self.salary}")
e1=Employee("Anu")
e2=Employee("Anusha",50000)
e1.display()
e2.display()
