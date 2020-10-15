def filter_long_words(lwords):
    length = list(map(len, lwords[0]))
    my_list = []
    for i in range(len(lwords[0])):
        if length[i] > lwords[1]:
            my_list.append(lwords[0][i])
    print("The list of word: ", my_list)

def main():
    words = input("Enter a list of words: ").split(",")
    n = int(input("Enter a digit: "))
    lwords = words, n
    filter_long_words(lwords)

main()
