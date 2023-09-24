print("---Compound Interest---")

principal = float(input("What is your initial deposit?: "))
interestRate = float(input("What is the annual interest rate?: "))
term = int(input("What is the term?: "))
years = int(input("How many years will the account be left to accrue interest?: "))

x = ((interestRate / 100) / term)+1
y = term * years

print(f"Your account balance will be {principal * x**y:,.2f}")
