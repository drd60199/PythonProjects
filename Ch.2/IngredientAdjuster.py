print("---Ingredient Adjuster---")

sugar = 1.5/48
butter = 1/48
flour = 2.75/48

cookieNumber = int(input("How many cookies do you want to make?: "))

print(f"""
You will need:
{sugar * cookieNumber:,.1f} cups of sugar
{butter * cookieNumber:,.1f} cups of butter
{flour * cookieNumber:,.1f} cups of flour
""")
