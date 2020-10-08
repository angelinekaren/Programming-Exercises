def calc_new_height():
    old_width = int(input("Enter the current width: "))
    old_height = int(input("Enter the current height: "))
    desired_width = int(input("Enter the desired width: "))
    aspect_ratio = old_width/old_height
    new_height = desired_width/aspect_ratio
    print("The corresponding height is: ", float(new_height))
    print(new_height)
    return new_height

calc_new_height()



