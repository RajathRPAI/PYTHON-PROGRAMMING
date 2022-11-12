# Program make a scientific calculator
# This program solves for some mathematical functions 0f numbers

import math as m
def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x/y
def modulus(x,y):
    return x%y
def power(x, y):
    return x**y
def sqrt(x):
    return m.sqrt(x)
def square(x):
    return x*x
def sin(x):
    return m.sin(x)
def cos(x):
    return m.cos(x)
def tan(x):
    return m.tan(x)
def ln(x):
    return m.log(x)
def log10(x):
    return m.log10(x)

print('''
1. additon
2. substraction
3. multiplication
4. division
5. modulus
6. power
7. square root
8. square
9. sin
10. cos
11. tan
12. ln
13. log10
''')
option = eval(input("\t what opeartion do you want to perform? \t "))
while option <= 13:
        if option ==1:
            print(" ********* Addition operation ***********")
            n1 = eval(input("Enter 1st no : "))
            n2 = eval(input("Enter the 2nd no: "))
            result = add(n1, n2)
            print(" the addition of {} and {} is {} ".format(n1, n2, result))
        elif option ==2:
            print(" ********* substraction operation ***********")
            n1 = eval(input("Enter 1st no : "))
            n2 = eval(input("Enter the 2nd no: "))
            result = subtract(n1, n2)
            print(" the substraction of {} and {} is {} ".format(n1, n2, result))
        elif option == 3:
            print(" ********* multiplication operation ***********")
            n1 = eval(input("Enter 1st no : "))
            n2 = eval(input("Enter the 2nd no: "))
            result = multiply(n1, n2)
            print(" the multiplication of {} and {} is {} ".format(n1, n2, result))
        elif option == 4:
            print(" ********* division operation ***********")
            n1 = eval(input("Enter 1st no : "))
            n2 = eval(input("Enter the 2nd no: "))
            result = divide(n1, n2)
            print(" the division of {} and {} is {} ".format(n1, n2, result))
        elif option == 5:
            print(" ********* modulus operation ***********")
            n1 = eval(input("Enter 1st no : "))
            n2 = eval(input("Enter the 2nd no: "))
            result =modulus(n1, n2)
            print(" the modulus of {} and {} is {} ".format(n1, n2, result))
        elif option == 6:
            print(" ********* power operation ***********")
            n1 = eval(input("Enter 1st no : "))
            n2 = eval(input("Enter the 2nd no: "))
            result = power(n1, n2)
            print(" the power of {} and {} is {} ".format(n1, n2, result))
        elif option == 7:
            print(" ********* square root operation ***********")
            n1 =eval(input("enter any number: "))
            result = sqrt(n1)
            print(" the square root of {} is {} ".format(n1, result))
        elif option == 8:
            print(" ********* square a number operation ***********")
            n1 =eval(input("enter any number: "))
            result = square(n1)
            print(" the square a number  of {} is {} ".format(n1, result))
        elif option == 9:
            print(" ********* sin operation ***********")
            n1 = eval(input("enter any number: "))
            result = sin(n1)
            print(" the sin value of of {} is {} ".format(n1, result))
        elif option == 10:
            print(" ********* cos operation ***********")
            n1 = eval(input("enter any number: "))
            result = cos(n1)
            print(" the cos value of {} is {} ".format(n1, result))
        elif option == 11:
            print(" ********* tan operation ***********")
            n1 = eval(input("enter any number: "))
            result = tan(n1)
            print(" the tan value of {} is {} ".format(n1, result))
        elif option == 12:
            print(" ********* ln operation ***********")
            n1 = eval(input("enter any number: "))
            result = ln(n1)
            print(" the lan value of {} is {} ".format(n1, result))
        elif option == 13:
            print(" ********* log of base 10 operation ***********")
            n1 = eval(input("enter any number: "))
            result = log10(n1)
            print(" the log of base 10 {} is {} ".format(n1, result))
        else:
            print(" INVALID INPUT \n PLS CHECK THE OPERATION NUMBER GIVEN \n ")
        print()
        new_option = eval(input("do you want continue other operation (yes- 1 or no-0): "))
        if new_option == 1:
            option = eval(input("\t what opeartion do you want to perform? \t "))
        else:
            print("**************** thank you so much.......**************** ")
            break
if option > 13:
    print(" INVALID INPUT \n PLS CHECK THE OPERATION NUMBER GIVEN \n AND GIVE THE INPUT 1 TO 11 ONLY\n RELAOD ")
