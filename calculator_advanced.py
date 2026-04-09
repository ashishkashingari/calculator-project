#Functions for operations
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply (a,b):
    return a*b
def divide(a,b):
    return a/b
while True:
    print("Calculator started")
    choice=input("Enter the operations(+,-,/,*): ").lower()
    try:
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))
    except ValueError:
      print("Invalid Number.\nPlease Enter a valid Number:")
      continue
    if choice=="+":
     print(add(num1,num2)) 
    elif choice== "-":
      print(subtract(num1,num2))
    elif choice=="*":
      print(multiply(num1,num2))
    elif choice=="/":
     if num2==0:
        print("Cannot divide by zero")
     else:
        print(divide(num1,num2))
    else:
     print("Invalid Operator.\nPlease Enter valid Operator.")
    again=input("Do you want to continue? (y/n):").lower()
    if again=="y":
     continue  
    elif again=="n":
       break 
