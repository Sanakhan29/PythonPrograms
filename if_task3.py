'''
Write a Python program to check second
number is completely divisible by first
number. Accept two integer values form
the user.(Hint:%)
'''

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if(num2%num1 == 0):
    print(num2,"is divisible by", num1)
