
def get_word_list_from_file():
    input_file = open('E:\\tmp\\test\\anagram\\sample.txt', 'r')
    word_list = input_file.read().splitlines()
    input_file.close()
    return word_list


def is_anagram(len_of_word1, sorted_word1, word2):
    return len_of_word1 == len(word2) and sorted_word1 == sorted(word2)


def end_of(word_list):
    return len(word_list) > 1


def get_first_word(word_list):
    return word_list[0]


def get_anagram_list_for_word(word1, word_list):
    sorted_word1 = sorted(word1)
    len_of_word1 = len(word1)
    anagram_list = []
    i = 0
    while len(word_list) > i:
        word2 = word_list[i]
        i += 1
        if is_anagram(len_of_word1, sorted_word1, word2):
            anagram_list.append(word2)
            word_list.remove(word2)
            i -= 1
    return anagram_list


def print_anagram_list_for_word(anagram_list, word1):
    if len(anagram_list) > 0:
            anagram_list.insert(0, word1)
            print(anagram_list)
            anagram_list.clear()


def main():
    word_list = get_word_list_from_file()
    while end_of(word_list):
        word1 = get_first_word(word_list)
        word_list.remove(word1)

        anagram_list = get_anagram_list_for_word(word1, word_list)

        print_anagram_list_for_word(anagram_list, word1)

#get first element from word list and remove it from word list
#search word list one by one if it have any anagram macthes
#get matched word from word list and remove it from word list
#then add it anagram list, collect anagramlist while end of the word list
#and print anagram list to screen
main()
