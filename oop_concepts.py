#*Getters and Setters*
class Bank_Account:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,balance):
        if balance>0:
            self.__balance=balance
        else:
            print("Invalid balance Sorry!")
b=Bank_Account("ann",100000)
print("balance",b.get_balance())
b.set_balance(2000000)
print("updated balance",b.get_balance())


#*Method Overloading*
class Calculator:
    def multiply_two(self,a,b,c=0):
        return a*b*c
    
c=Calculator()
print(f"The value of multiplication of two number:{c.multiply_two(6,2)}")
print(f"The value of multiplication of three number:{c.multiply_two(1,2,8)}")


#*Method Overriding*
class Shape:
    def draw(self):
        print("Drawing shape!")
class Circle(shape):
    def draw(self):
        print("Drawing circle!")
s=Shape()
s.draw()
c=Circle()
c.draw()


#*Abstract Classes*
from abc import ABC , abstractmethod
class employe(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Manager(employe):
    def __init__(self,hour,rate):
        self.hour=hour
        self.rate=rate
    def calculate_salary(self):
        return self.hour*self.rate
m=Manager(9,4000)
print("salary:",m.calculate_salary())
