print("---Roulette Wheel Colors---")

number = int(input("Enter a number in the range of 0 to 36: "))

if number == 0:
    print("The pocket is green")
elif number >= 1 and number <= 10:
    if number % 2 == 0:
        print("The pocket is black")
    if number % 2 != 0:
        print("The pocket is red")
elif number >= 11 and number <= 18:
    if number % 2 == 0:
        print("The pocket is red")   
    if number % 2 != 0:
        print("The pocket is black")
elif number >= 19 and number <= 28:
    if number % 2 == 0:
        print("The pocket is black")
    if number % 2 != 0:
        print("The pocket is red")
elif number >= 29 and number <= 36:
    if number % 2 == 0:
        print("The pocket is red")
    if number % 2 != 0 :
        print("The pocket is black")
else:
    print("Error")



