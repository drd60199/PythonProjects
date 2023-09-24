end = int(input("How hight should I go?: "))
print()
print("Number\t\tsquare")
print("------------------------")
for number in range(1, end + 1):
    square = number ** 2
    print(f"{number}\t\t{square}")