n = int(input('Enter the number of items: '))
myDict = {}
keys = input("Enter the keys by comma: ").split(",")
values = input("Enter the values by comma: ").split(",")
keyList = input("Enter the key: ").split(",")

def remove_keys(myDict, keyList):
    for x in range(n):
        myDict[keys[x]] = values[x]
    for key in keyList:
        if key in myDict.keys():
            myDict.pop(key)
    return myDict

def main():
    print(remove_keys(myDict, keyList))

main()