print("---Color Mixer---")
color1 = input("What is the first color?: ")
color2 = input("What is the second color?: ")

if color1 == "red":
    if color2 == "blue":
        print("purple")
    elif color2 == "yellow":
        print("Orange")
    elif color2 == "red":
        print("Red")
    else:
        print("Error")

if color1 == "blue":
    if color2 == "red":
        print("Purple")
    elif color2 == "yellow":
        print("Green")
    elif color2 == "blue":
        print("blue")
    else:
        print("Error")

if color1 == "yellow":
    if color2 == "blue":
        print("Green")
    elif color2 == "red":
        print("Orange")
    elif color2 == "yellow":
        print("Yellow")
    else:
        print("Error")


    