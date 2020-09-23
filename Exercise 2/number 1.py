print("Enter your height")
feet = int(input("Feet:"))
inches = int(input("Inches:"))

# the height is in inches
height = (feet*12)+inches
# the length of snowboard is in centimeters
boardlength = height*2.54*0.88

print("Suggested board length:", boardlength, "cm")