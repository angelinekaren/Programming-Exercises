def translate(text):
    vowels = "aiueo "
    string_for_text = ""
    for x in text:
        if x in vowels:
            string_for_text += x
        else:
            string_for_text += x + "o" + x
    return string_for_text


def main():
    print(translate("this is fun"))


main()
