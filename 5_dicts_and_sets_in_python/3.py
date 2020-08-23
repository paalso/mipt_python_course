# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab23.html#o3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab18.html#o4

# Упражнение № 3. Подсчет слов
# =============================
"""
Дан текст на некотором языке. Требуется подсчитать сколько раз каждое слово
входит в этот текст и вывести десять самых часто употребяемых слов в этом
тексте и количество их употреблений.

В качестве примера возьмите файл с текстом лицензионного соглашения Python
/usr/share/licenses/python/LICENSE.
"""

# def read_file():

import string

book_file = "de Saint-Exupery Antoine. The Little Prince - royallib.ru.txt"
with open(book_file, "r") as in_file:
    text = in_file.read()

text = text.lower()
for symbol in string.punctuation:
    text = text.replace(symbol, " ")
text_words = text.split()

text_dict = {}
for word in text_words:
    text_dict[word] = text_dict.get(word, 0) + 1

most_frequent = sorted(
    zip(text_dict.keys(), text_dict.values()), key=lambda p: -p[1])

for word, freqcy in most_frequent[:20]:
    print("{:<5}\t\t{:>4}".format(word, freqcy))
