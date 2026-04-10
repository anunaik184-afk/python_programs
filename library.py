class library:
    def __init__(self,Book_name,Book_count,Book_ID,Time):
        self.Book_name=Book_name
        self.Book_count=Book_count
        self.Book_ID=Book_ID
        self.Time=Time
    def borrow(self):
        if self.Book_count>0:
            choice=input("Do you want to borrow the book!: ").lower()
            if choice=="yes":
                self.Book_count-=1
                print(f"you borrow {self.Book_name}:(ID:{self.Book_ID}) ")
                print(f"Book left:{self.Book_count}")
            else:
                print("You didn't borrow any book !")
        else:
            print("No books are available to borrow")
    def return_book(self):
        return_time=input("Enter what time you return the book(AM/PM)!:").upper()
        if return_time==self.Time:
            print("You return the book on time . No penalty!")
        else:
            print("you didn't return the book on time . You have to pay  ₹500 penalty")
        self.Book_count+=1
        print(f"Number of books after returning:{self.Book_count}")
    def show_Book(self):
        print("----BOOK DETAILS-----")
        print(f"Book_Name:{self.Book_name}\nBook_ID:{self.Book_ID}\nAvailable_Books:{self.Book_count}")
l=library("Python_basics",10,"56","10AM")
while True:
    print("\n----LIBRARY MENU-----")

    print("1.Boorow\n2.Returning\n3.Show_Book\n4.Exit")

    choice=input("Enter your choice(1-4): ").strip()
    if choice=='1':
        l.borrow()
    elif choice=='2':
        l.return_book()
    elif choice=='3':
        l.show_Book()
    elif choice=='4':
        print("---EXITING---")
        break
    else:
        print("Invalid choice ! try again")
    



    
