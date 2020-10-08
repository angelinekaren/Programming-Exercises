print("Divide students in 3 classes into groups")

class1 = int(input("Enter the number of student in class 1 >>"))
class2 = int(input("Enter the number of student in class 2 >>"))
class3 = int(input("Enter the number of student in class 3 >>"))

dividedgroup1 = int(input("Enter the number of groups in class 1 >>"))
dividedgroup2 = int(input("Enter the number of groups in class 2 >>"))
dividedgroup3 = int(input("Enter the number of groups in class 3 >>"))

group1 = class1 // dividedgroup1
group2 = class2 // dividedgroup2
group3 = class3 // dividedgroup3

leftover1 = class1 % dividedgroup1
leftover2 = class2 % dividedgroup2
leftover3 = class3 % dividedgroup3

print("Number of students in each group:")
print(" Class 1:", group1, "\n", "Class 2:", group2, "\n", "Class 3:", group3)
print("Number of students leftover:")
print(" Class 1:", leftover1, "\n", "Class 2:", leftover2, "\n", "Class 3:", leftover3)