print("---Male and Female Percentages---")

males = int(input("How many males are in the class?: "))
females = int(input("How many females are in the class: "))

total = males + females

print(f"""
The class is {(males / total)*100:,.2f}% males and {(females / total)*100:,.2f}% females""")
