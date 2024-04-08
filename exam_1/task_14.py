# 14.	Напишите программу, которая принимает текст и
# выводит два слова: наиболее часто встречающееся и самое длинное.

text = input('Введите текст: ').lower()

punctuation = {'!', '-', '?', ':', ',', ';', '.'}
i = len(text) - 1
while i >= 0:
    if text[i] in punctuation:
        text = text[:i] + text[i+1:]
    i -= 1

word_count = {}
for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_frequent_word = ''
max_count = 0
for word, count in word_count.items():
    if count > max_count:
        max_count = count
        most_frequent_word = word
print(f'Наиболее часто встречающееся слово: "{most_frequent_word}". Встречается {max_count} раз(а).')

longest_word = ''
for word in text.split():
    if len(word) > len(longest_word):
        longest_word = word
print(f'Самое длинное слово: "{longest_word}". Его длина {len(longest_word)} символа(ов).')
