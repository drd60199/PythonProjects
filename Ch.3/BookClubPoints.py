print("---Book Club Points---")

bookNumber = int(input("Enter the numer of books that you have purchaced this month: "))

if bookNumber == 0 or 1:
    print("You have earned 0 points.")
elif bookNumber >= 2 or 3:
    print("You have earned 5 points.")
elif bookNumber == 4 or 5:
    print("You have earned 15 points.")
elif bookNumber == 6 or 7:
    print("You have earned 30 points.")
elif bookNumber >= 8:
    print("You have earned 60 points.")
