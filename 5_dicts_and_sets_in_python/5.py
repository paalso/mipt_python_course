# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab23.html#o5
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab18.html#o5

# Упражнение № 5. Страны и языки
# ===============================

# Дан список стран и языков на которых говорят в этой стране в формате
# <Название Страны> : <язык1> <язык2> <язык3> ... в файле task5/input.txt.
# На ввод задается N - длина списка и список языков. Для каждого языка укажите,
# в каких странах на нем говорят.

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
            country, langs = line.split(" : ")
            dictionary[country] = langs.split()
    return dictionary


country_lang_dict = load_dict("countries_langs.txt")
lang_country_dict = reverse_dict(country_lang_dict)

langs = []
n = int(input())
for _ in range(n):
    langs.append(input())

for lang in langs:
    print(*lang_country_dict[lang] if lang in lang_country_dict else "-")
