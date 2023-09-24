print("---Restaurant Selector---")

vegetarian = input("Are any of the members in your party vegetarian?: ")
vegan = input("Are any of the members in your party vegan?: ")
glutenFree = input("Are any of the members in your party gluten-intolerant?: ")

allRestaurants = [
"Joe's Gourmet Burgers",
"Main Street Pizza Company",
"Corner Cafe",
"Mama's Fine Italian",
"The Chef's Kitchen",
]

vegetarianRestaurants = [
"Main Street Pizza Company",
"Corner Cafe",
"Mama's Fine Italian",
"The Chef's Kitchen",
]
glutenFreerestaurants = [
"Main Street Pizza Company",
"Corner Cafe",
"The Chef's Kitchen",
]
veganRestaurants = [
"Corner Cafe",
"The Chef's Kitchen",
]

if vegetarian == "yes" and vegan == "no" and glutenFree == "no":
    print(vegetarianRestaurants)
elif vegan == "yes" and glutenFree == "no":
    print(glutenFreerestaurants)
elif glutenFree == "yes":
    print(glutenFreerestaurants)
elif vegetarian == "no" and vegan == "no" and glutenFree == "no":
    print(allRestaurants)





