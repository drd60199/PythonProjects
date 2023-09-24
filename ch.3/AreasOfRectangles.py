print("---Areas of Rectangles---")

lengthOne = float(input("What is the length of rectangle one?: "))
widthOne = float(input("Wht is the width of rectangle one?: "))

lengthTwo = float(input("What is the length of rectangle two?: "))
widthTwo = float(input("What is the width of rectangle two?: "))

areaOne = lengthOne * widthOne
areaTwo = lengthTwo * widthTwo

if areaOne < areaTwo:
    print("Rectangle Two is larger!")
elif areaOne > areaTwo:
    print("Rectangle One is larger")
elif areaOne == areaTwo:
    print("The Rectangles are the same!")
