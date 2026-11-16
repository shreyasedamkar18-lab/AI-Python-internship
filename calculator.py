def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "cannot divide by zero"
    return a/b

print("----SIMPLE CALCULATOR----")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

choice = int(input("enter your choice(1-4):"))

num1=float(input("enter first number:"))
num2=float(input("enter second number:"))

if choice==1:
    print("result:",add(num1,num2))
elif choice==2:
    print("result:",subtract(num1,num2))
elif choice==3: 
    print("result:",multiply(num1,num2))
elif choice==4:
    print("result:",divide(num1,num2))
else:
    print("invalid choice!")
    