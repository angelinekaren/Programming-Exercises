import re


def hapax(for_word, count):
    for word in for_word:
        count.setdefault(word, 0)
        count[word] += 1
    return count


def hapax_freq(count):
    for words_count in count:
        if count[words_count] == 1:
            print(words_count)


if __name__ == "__main__":
    file = open("TheGreatGreenBlight.txt", "r", encoding="utf-8")
    for_word = re.findall('\w+', file.read().lower())
    count = {}
    hapax(for_word, count)
    hapax_freq(count)
