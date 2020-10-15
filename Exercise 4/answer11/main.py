def char_freq(str):
    dictionary = {}
    for i in range(len(str)):
        if str[i] in dictionary:
            dictionary[str[i]] = dictionary.get(str[i])+1
        else:
            dictionary[str[i]] = 1
    return dictionary


def main():
    str = input("Enter a word: ")
    print(char_freq(str))

main()
