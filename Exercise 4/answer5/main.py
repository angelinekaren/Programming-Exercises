def main():
    lst1 = input("Enter a list:").split(",")
    lst2 = input("Enter a list:").split(",")
    print(overlapping(lst1, lst2))


def overlapping(lst1, lst2):
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                return True
    return False

#def overlapping(lst1, lst2):
    #for i in lst1:
        #for j in lst2:
            #if i == j:
                #return True
    #return False

main()





