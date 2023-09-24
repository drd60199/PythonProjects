print("---Software Sales---")

packages = int(input("How many packages do you plan to purchase?: "))

total = packages * 99

if packages >= 10 and packages <= 19:
    discount = 0.10 * total
    print(f"Your discount is ${discount:,.2f} for a total of ${total - discount:,.2f}.")
elif packages >=20 and packages <= 49:
    discount = 0.20 * total
    print(f"Your discount is ${discount:,.2f} for a total of ${total - discount:,.2f}.")
elif packages >= 50 and packages <= 99:
    discount = 0.30 * total
    print(f"Your discount is ${discount:,.2f} for a total of ${total - discount:,.2f}.")
elif packages >= 100:
    discount = 0.40
    print(f"Your discount is ${discount:,.2f} for a total of ${total - discount:,.2f}.")
