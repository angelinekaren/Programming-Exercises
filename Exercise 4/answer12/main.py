def makeForms(verb):
    character = ('o', 'ch', 's', 'sh', 'x', 'z')
    if verb.endswith("y"):
        new = verb[:-1] + "ies"
    elif verb.endswith(character):
        new = verb + "es"
    else:
        new = verb + "s"
    return new


def main():
    verb = input("Enter your word: ")
    print("The third person singular form is", makeForms(verb))

main()