print("---Magic Dates--")

month = int(input("Enter a numeric month: "))
day = int(input("Enter a day: "))
year = int(input("Enter a 2 digit year: "))

if month * day == year:
    print("This is a magic date!")
else:
    print("This is not a magic number")