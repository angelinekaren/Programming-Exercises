n = int(input("Enter the number of items: "))
myDict = {}
keys = input("Enter the keys by comma: ").split(",")
values = input("Enter the values by comma: ").split(",")

def for_dict():
    for x in range(n):
        myDict[keys[x]] = values[x]
    return myDict

print(for_dict())

def find_value(myDict, val):
    a_list = []
    for key in myDict.keys():
        if val == myDict[key]:
            a_list.append(key)
    return a_list

def main():
    val = input("Enter a value you want to search: ")
    print(find_value(myDict, val))

main()
