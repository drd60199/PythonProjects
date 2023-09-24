print("---Mass And Weight---")

mass = float(input("Enter the object's mass: "))

weight = mass * 9.8

print(weight,"newtons")

if weight > 500:
    print("The object is too heavy.")
elif weight < 100:
    print("The object is too light.")