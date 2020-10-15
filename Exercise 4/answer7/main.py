def maps_a_list(words):
    list_integers = map(len, words)
    return list(list_integers)


def main():
    words = input("Enter a list of words: ").split(",")
    print("The lengths of the corresponding words are", maps_a_list(words))


main()
