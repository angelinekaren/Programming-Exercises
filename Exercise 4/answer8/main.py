def find_longest_word(words):
    length = list(map(len, words))
    return max(length)

def main():
    words = input("Enter a list of words: ").split(",")
    print("The length of the longest word is", find_longest_word(words))

main()


