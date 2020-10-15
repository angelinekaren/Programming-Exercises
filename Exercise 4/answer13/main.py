def makeForming(word):
    if word.endswith("ie"):
        return word[:-2] + "ying"
    elif word[-2:] == 'ee':
        return word + "ing"
    elif word == 'be':
        return word + "ing"
    elif word.endswith("e"):
        return word[:-1] + "ing"
    vowels = ['a', 'i', 'u', 'e', 'o']
    if word[-1] not in vowels:
        if word[-2:-1] in vowels:
            if word[:-2] not in vowels:
                return word + str(word[-1]) + "ing"
    return word + "ing"

def main():
    word = input("Enter a word: ")
    print("The present participle form is", makeForming(word))

main()

