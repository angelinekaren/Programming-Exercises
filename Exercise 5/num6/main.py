def rotate_13(for_texts):
    key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x',
           'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b',
           'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm',
           'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
           'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D',
           'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I',
           'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}
    for_strings = ""
    for x in range(len(for_texts)):
        if for_texts[x] in key:
            for_strings += key[for_texts[x]]
        else:
            for_strings += for_texts[x]
    return for_strings

def main():
    for_texts = input('Enter texts you want to encode/decode: ')
    print(rotate_13(for_texts))

main()

