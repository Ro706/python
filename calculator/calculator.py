import os
def sum():
    a = []
    sum = 0
    a = input("enter number:").split(sep=" ")
    for i in a:
        sum +=int(i)
    print("sum =",sum)  
def sub():
    a = []
    subtract = 0
    a = input("enter number:").split(sep=" ")
    for i in a:
        subtract -=int(i)
    print("subtract =",subtract)
def div():
    a = input("enter number:").split(sep =" ")
    div = 0
    for i in a:
        div /= int(i)
    print("div :",div)
def mul():
    a = input("enter number:").split(sep = " ")
    mul = 1
    l = len(a)
    n = len(a)
    for i in a:
        a[l-n] = int(a[l-n])
        n -= 1
    for i in a:
        mul *= i        
    print(mul)
def user_menu():
    print("--> sum")
    print("--> sub")
    print("--> div")
    print("--> mul")
    print("--> exit")
    print("--> clear")      
loop = 1
while loop != 0:
    user_menu()  
    user = input("enter your choice:")
    if user == "sum":
        sum()
    elif user == "sub":
        sub()
    elif user == "div":
        div()
    elif user == "mul":
        mul()
    elif  user == "exit":
        print("thank you for using me")
        loop = 0
    elif user == "clear":
        os.system("cls")
    else:
        print("error")
        pass                                  
