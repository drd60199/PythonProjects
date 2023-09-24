print("---February Days---")

year = int(input("Enter a year: "))

if year % 100 == 0 and year % 400 == 0:
    print("There are 29 days in February.")
elif year % 100 != 0 and year % 4 == 0:
    print("There are 29 days in February.")
else:
    print("There are 28 days in February.")