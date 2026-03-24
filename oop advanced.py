balance=0
while True:
    print("***Banking System***\n1.Check_balance\n2.Deposit Money\n3.Withdraw\n4.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print(f"The total balance:{balance}")
    elif choice==2:
        amount=int(input("Enter the amount which you  deposit: "))
        balance+=amount
        print(f"After deposited money:{balance}")
    elif choice==3:
        amount=int(input("Enter the amount which you  withdraw: "))
        if amount<=balance:
            balance-=amount
            print(f"After withdrawing money:{balance}")
        else:
            print("You dont have sufficient money")
    elif choice==4:
        print("Thank you for visiting")
        break
    else:
        print("Ivalid Choice!")




Students=[]
while True:
    print("***Education System***\n1.Add student\n2.Display student\n3.Exit")
    choice=int(input("Enter your choice which you want to choose:"))
    if choice==1:
        name=input("Enter name of the student: ")
        age=int(input("Enter age of the student: "))
        course=input("Enter the course of the student: ")
        Student = {
            "name": name,
            "age": age,
            "course": course
        }
        Students.append(Student)
        print("Student details added successfully! ")
    elif choice==2:
        if not Students:
            print("No student record found!")
        else:
            for s in Students:
                print("\nName:",s["name"])
                print("Age:",s["age"])
                print("Cource:",s["course"])
    elif choice==3:
        print("---EXIT---")
        break
    else:
        print("Invalid Choice")


