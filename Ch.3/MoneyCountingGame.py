print("---Money Counting Game---")

pennies = float(input("Enter the number of pennies: "))
nickles = float(input("Enter the number of nickles: "))
dimes = float(input("Enter the number of dimes: "))
quarters = float(input("Enter the number of quarters: "))

pennyTotal = pennies * 0.01
nickleTotal = nickles * 0.05
dimeTotal = dimes * 0.10
quarterTotal = quarters *0.25

totalChange = pennyTotal + nickleTotal + dimeTotal + quarterTotal

if totalChange == 1.00:
    print("Congratulations! You made a dollar.")
elif totalChange > 1.00:
    print("You exceeded a dollar.")
elif totalChange < 1.00:
    print("You made less than a dollar.")