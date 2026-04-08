#Functions for operations
def Addition(a,b):
    return a+b
def Subtract(a,b):
    return a-b
def Multiply (a,b):
    return a*b
def Divide(a,b):
    return a/b
#Main loop to keep calculator running
while True:
 #Taking user input
 choice=input("Enter the choice: Addition , Subtract , Multiply , Divide : ")
 #Taking numbers from users
 num1=float(input("Enter the number:"))
 num2=float(input("Enter the number:"))
#Performing operatons based on choice
 if choice=="Addition":
  print(Addition(num1,num2)) 
 
 elif choice== "Subtract":
     print(Subtract(num1,num2))
 elif choice=="Multiply":
    print(Multiply(num1,num2))
 elif choice=="Divide":
    print(Divide(num1,num2))
 else:
    print("Error")
    #Ask user if they want to continue
 again=input("Do you want to continue? (y/n):")
 if again=="y":
  continue
 elif again=="n":
      break 
else:
  print("Invalid input")
