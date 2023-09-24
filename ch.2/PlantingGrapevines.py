print("---Planting Grapevines---")

length = float(input("What is the length of the row in feet?: "))
endPost = float(input("What is the amount of space in feet, occupied by an end-post assembly?: "))
betweenVines = float(input("What is the space in between the vines in feet?: "))
x = length - (2*endPost)
y = betweenVines

print(f"The row will fit {x/y:,.0f} grapevines")