num = int(input("Enter the total numbers you want to enter : "))
cube = 0
for i in range(num) :
    a = int(input("Enter the number :"))
    cube = cube + a*a*a
    average = cube / num
print("\n Sum of the cubes of the numbers:",cube)
print("\n Average of Sum of the cubes of the numbers : ", average)
print()
new_option = eval(input("Do you want continue other CUBE operation (yes- 1 or no-0): "))
if new_option == 1:
    num =int(input("Enter the total numbers you want to enter : "))
    square = 0
    for i in range(num):
        a = int(input("Enter the number : "))
        square = square + a * a
        average = square / num
    print("\nSum of the cubes of the numbers : ", square)
    print("\n Average of Sum of the cubes of the numbers : ", average)
else:
    print("**************** THANK YOY SO MUCH **************** ")

