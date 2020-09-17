# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab23.html#o6
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab18.html#o6

# Упражнение № 6. Сделать русско-английский словарь
# ==================================================

# В файле http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task6/en-ru.txt
# находятся строки англо-русского словаря
# Требуется создать русско-английский словарь и вывести его в файл ru-en.txt
# в таком формате:
# делать - to do
# дом - home...
# Порядок строк в выходном файле должен быть словарным с человеческой точки
# зрения (так называемый лексикографический порядок слов).
# То есть выходные строки нужно отсортировать.


# В предоставленном словаре какие-то ошибки, - придется чуть почистить
def refine_string(text):
    amiss_symbols = "=,.-'!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in amiss_symbols:
        if c in text:
            text = text.replace(c, "")
    return text


def reverse_dict(dictionary):
    "Reversing of a dict in the formar {key: [values]}"
    from collections import defaultdict
    reversed_dict = defaultdict(lambda : [])
    for key, values in dictionary.items():
        for val in values:
            reversed_dict[val].append(key)
    return dict(reversed_dict)


def load_dict(dict_file):
    dictionary = {}
    with open(dict_file, "r", encoding="utf-8") as in_file:
        for line in in_file:
            word, translation = line.split("\t-\t")
##            if "," in translation:
##                print(translation)
            dictionary[word] = refine_string(translation.rstrip())
    return dictionary


dict_en_ru = load_dict("en-ru.txt")

dict_en_ru_refined_file = "en-ru-refined.txt"
with open(dict_en_ru_refined_file, "w", encoding="utf8") as out_file:
    for word in sorted(dict_en_ru.keys()):
        print("{}\t-\t  {}".format(word, dict_en_ru[word]), file=out_file)

dict_ru_en = {dict_en_ru[eng_word]: eng_word for eng_word in dict_en_ru}


dict_ru_en_file = "ru-en.txt"
with open(dict_ru_en_file, "w", encoding="utf8") as out_file:
    for word in sorted(dict_ru_en.keys()):
        print("{}\t-\t  {}".format(word, dict_ru_en[word]), file=out_file)
