print("---Body Mass Index---")

height = float(input("What is your height in inches?: "))
weight = float(input("What is you weight in pounds?: "))

BMI = weight * 703/height**2

if BMI >= 18.5 and BMI <= 25:
    print(f"{BMI:.2f}:You have an optimal BMI.")
if BMI < 18.5:
    print(f"{BMI:.2f}:You are underweight.")
if BMI > 25:
    print(f"{BMI:.2f}:You are overweight.")