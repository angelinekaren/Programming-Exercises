import string


# lowercase and uppercase are considered the same


def check_pangram(sentence):
    alphabet = string.ascii_uppercase  # can be change into lowercase
    for words in alphabet:
        if words not in sentence.upper():  # can be change into lower, but make sure it's the same with the alphabet
            return False
    return True


def main():
    sentence = input("Input your sentence here to check: ")
    if check_pangram(sentence) == True:
        print("The sentence is a pangram.")
    else:
        print("The sentence is not a pangram.")


main()

