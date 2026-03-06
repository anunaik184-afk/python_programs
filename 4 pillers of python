#**Abstraction**:
 

class phone:
    def __init__(self):
        print("phone is good")
    
    def call_contact(self):
        print(" i made new call contacts in my phone")
    def take_picture(self):
        print("it has very good camera to take pictures")
p=phone()
p.call_contact()
p.take_picture()



#**Inheritance**:
#1.
class Humans:
    def __init__(self,eating):
        self.eating=eating
    def eat(self):
        print(f"{self.eating}  eating is done")
class dog(Humans):
    def not_eating(self):
        print(f"{self.eating} cant compleate fully")
d=dog("chicken")    
d.not_eating()


2.#Create a base class `Vehicle` with a `start` method. Then create a subclass `Bike` with an additional `ride()` method.
#Demonstrate how the `Bike` can use both `start` and `ride`.

class vehicle:
    def start(self):
        print("vehicle start ")

class bike(vehicle):
    def ride(self):
        print("bike is allready ride")
b=bike()
b.ride()
b.start()

#**Polymorphism**:
#1.
class Human:
    def eat(self):
        print("Human eating")
class parent:
    def eat(self):
        print("parents are eating")
class children:
    def eat(self):
        print("childrens are eating")

Human=[parent(),children()]    
for h in Human:
     h.eat()

2.#Implement a `Shape` class and derive `Circle` and `Rectangle` classes with a method `calculate_area`. Each class should calculate area differently based on its shape.
# Create a loop to calculate areas for both `Circle` and `Rectangle` objects

import math
class shape:
    def calculate_area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        return math.pi*self.radius*self.radius
class Rectangle:
    def __init__(self,length,width):
        self.length=length  
        self.width=width
    def calculate_area(self):
        return self.length*self.width
    
c1=circle(3)
r1=Rectangle(3,4)   
shapes=[c1,r1]
for shape in shapes:
    print("Area:",shape.calculate_area())



#**Encapsulation**:
 #Create a `BankAccount` class with private attributes for `account_number` and `balance`.
 #Add methods to check balance, deposit, and withdraw funds.
 #Try accessing the balance directly and observe the result.


class Bank_Account:
    def __init__(self,account_number,balance):
        self.__account_number=account_number #Private attribute
        self.balance=balance
    def check_balance(self):
        print(f"total balance is {self.balance}")

    def deposit(self,ammount):
        self.balance+=ammount
        (f"tottal balance after deposit is{self.balance}")
    def withdraw(self,ammount):
        if ammount<=self.balance:
            self.balance-=ammount
            print(f"remaining balance after withdraw {self.balance}")
        else:
            print("Insufficient money")    
B=Bank_Account("anu123",30000)
B.check_balance()
B.withdraw(100)
B.deposit(10000)










