print("---Shipping Charges---")

weight = float(input("What is the weight of your package in pounds?: "))

if weight <= 2:
    print("Charges: $1.50.")
elif weight > 2 and weight <= 6:
    print("Charges: $3.00")
elif weight > 6 and weight <= 10:
    print("Charges: $4.00")
elif weight > 10:
    print("Charges: $4.75")

