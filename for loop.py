# Multiples of 3:

for i in range(3, 4):
    for j in range(1, 31):
        print(f"{i} X {j}: {i*j}")

#Print Your Name Letter by Letter:

name="Anu Naik"
for letter in name:
    print(letter)


#Sum of First 10 Numbers:
sum=0
for i in range(1,11):
    sum+=i
print(f"Tottal sum:{sum}")

#Count Vowels in a String:

sentence=input("Enter your sentence what you want: ")
count=0
for ch in sentence:
    if ch in "AEIOUaeiou":
        count+=1
        print(ch) #for geting vowels
print(f"Number of vowels:{count}") # for getting count of vowels
