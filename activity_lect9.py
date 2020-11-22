#MAKE A TABLE OF Num that user entered

num = int(input("Enter Number:"))

print("----Table of" , num , "----")
for i in range(0,11):
    print(num , "*" , i , "=" , num*i)