print("---Total Purchase---")
tax = 0.07
itemOne = float(input("What is the price of item 1: "))
itemTwo = float(input("What is the price of item 2: "))
itemThree = float(input("What is the price of item 3: "))
itemFour = float(input("What is the price of item 4: "))
itemFive = float(input("What is the price of item 5: "))

subTotal = itemOne + itemTwo + itemThree + itemFour + itemFive
taxAmount = subTotal * tax
total = subTotal + taxAmount

print(f"Your subtotal is ${subTotal:,.2f}")
print(f"Tax paid is ${taxAmount:,.2f}")
print(f"Total is ${total:,.2f}")
