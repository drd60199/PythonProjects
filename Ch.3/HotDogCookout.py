print("---Hot Dog Cookout Calculator---")

import math

people = int(input("How many people will be attending the cookout?: "))
hotdogNumber = int(input("How many hotdogs will each person get?: "))

hotdog = 10
bun = 8

requiredDogspack = (hotdogNumber * people)/10
requiredBunspack = (hotdogNumber * people)/8


adjustedDogspack = (math.ceil(requiredDogspack))
adjustedBunspack = (math.ceil(requiredBunspack))
leftoverDogs = (adjustedDogspack*10)-(people * hotdogNumber)
leftoverBuns = (adjustedBunspack*8)-(people * hotdogNumber)


print(adjustedDogspack, "Pack(s) of hotdogs.")
print(adjustedBunspack, "Pack(s) of buns.")
print(leftoverDogs, "Leftover hotdog(s).")
print(leftoverBuns, "Leftover bun(s).")


