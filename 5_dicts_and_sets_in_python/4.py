#
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab18.html#o4

# Упражнение № 4. Перевод текста
# ===============================


# Дан словарь task4/en-ru.txt с однозначным соответствием
# английских и русских слов
dict_url = "http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task4/en-ru.txt"
# Дан текст для перевода
text_url = "http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task4/input.txt"
# Сделать подстрочный перевод с помощью имеющегося словаря и вывести результат
# в output.txt. Незнакомые словарю слова нужно оставлять в исходном виде.

import string

STOP_WORDS = ("a", "the")

def handle_word(word):
    punctuation_after_word = ""
    while True:
        i = len(word) - 1
        if word[i] not in string.punctuation:
            break
        punctuation_after_word += word[i]
        word = word[:-1]

    # case_info = (is the word uppercase? is the word capitalized?)
    case_info = (word.isupper(), word[0].isupper())
    return (word.lower(), "".join(reversed(punctuation_after_word)), case_info)


def translate_word(word, dictionary, stop_words):
    if word in stop_words:
        return ""
    word, punctuation, case_info = handle_word(word)
    if word in dictionary:
        word = dictionary[word]
    is_uppercased, is_сapitalized = case_info
    if is_uppercased:
        word = word.upper()
    elif is_сapitalized:
        word = word.capitalize()
    return word + punctuation


def load_dict(dict_file):
    dictionary = {}
    with open(dict_file, "r", encoding="utf-8") as in_file:
        for line in in_file:
            engword, ruword = line.split("\t-\t")
            dictionary[engword] = ruword.rstrip()
    return dictionary


dict_file = "en-ru.txt"
text_file = "input.txt"
dict_en_ru = load_dict(dict_file)

out_file = open("output.txt", "w", encoding="utf-8")
with open(text_file, "r", encoding="utf-8") as in_file:
    for line in in_file:
        words = line.split()
        translated_words = list(map(lambda w: translate_word(w, dict_en_ru, STOP_WORDS), words))
        print(" ".join(translated_words), file=out_file)
out_file.close()
