#1. Basic Counting with `while` Loop:
#Write a program that counts from 1 to 10 using a `while` loop.
i=1
while i<=10:
    print(i)
    i+=1    

#2.KSRTC Bus Seats Availability

#Let’s say you want to simulate a KSRTC bus seat booking system. The bus has 5 available seats. Each time a seat is booked, the available seats decrease.
#seat
available_seat=5
while available_seat>0:
    print(f"{available_seat} seats are available for booking!")
    booking=input("Do you want to book the seat(Yes/No):")
    if booking=="Yes":
        available_seat-=1
        print("Seat booked! Tank you")
    else:
        print("No booking made!") 
print("All seats are booked!")      

#3.Odd Numbers Printer:
#Create a program that prints all odd numbers between 1 and 20 using a `while` loop.
i=1
while i<=20:
  if i/2!=0:
    print(i)
    i+=1
  else:
    break
  i+=1  
        



