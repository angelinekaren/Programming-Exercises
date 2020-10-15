def histogram(lst):
    for i in range(0, len(lst)):
        print(int(lst[i]) * '*')

def main():
    lst = input("Enter a list: ").split(",")
    histogram(lst)

main()


