def menu():
    print(" ###Simple Calculation###\n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Dvide \n 5.Exit")
while True:
    menu()
    choice=input("Enter your choice(1-5): ")
    if choice in ['1','2','3','4',]:
        try:
            num1=int(input("Enter first number: "))
            num2=int(input("Enter second number: "))
        except ValueError:
            print("Invalid Input! pleas enter numerical values.")
            continue
    if choice=='1':
        print(f"Sum of the two numbers:",num1+num2)
    elif choice=='2':
        print(f"The value of suntraction is:",num1-num2)
    elif choice=='3':
        print(f"The value of Multiplication is:",num1*num2)
    elif choice=='4':
        print(f"The value of Division is:",num1/num2)
    elif choice=='5':
        break
    else:
        print("Invalid choice please Try again!")
        




    

