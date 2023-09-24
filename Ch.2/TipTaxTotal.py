print("---Tip Tax and Total---")

foodPrice = float(input("How much was your meal?: "))
tip = foodPrice * 0.18
tax = foodPrice * 0.07
total = foodPrice + tip + tax

print(f"""
The tip for your meal is ${tip:,.2f}
The tax for your food is ${tax:,.2f}
The total for your meal is ${total:,.2f}
""")
 