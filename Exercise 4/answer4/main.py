def main():
    the_value = input("Enter a value: ")
    the_list = input("Enter values: ").split(",")
    val = the_value, the_list
    is_member(val)


def is_member(val):
    for i in range(len(val[1])):
        if val[0] == val[1][i]:
            return print("True")
            break
    return print("False")


main()


