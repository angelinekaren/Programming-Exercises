def word_frequencies(my_list):
    for_dict = {}
    for word in my_list:
        for_dict.setdefault(word, 0)
        for_dict[word] += 1
    return for_dict

def main():
    my_list = input("Enter strings by comma: ").split(",")
    print(word_frequencies(my_list))

main()
