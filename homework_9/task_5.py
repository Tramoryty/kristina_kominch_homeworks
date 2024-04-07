# 5) Выведите статистику частности букв в кортеже
# long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и’,'и', 'и', 'т', 'т', 'а', 'и', 'и','и', 'и', 'и', 'т', 'и’)
# Примечание: Статистика частности - число повторений каждой из букв.

long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и','и', 'и', 'и', 'т', 'и')
letter_count = {}
for letter in long_word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
for letter, count in letter_count.items():
    print(f'Буква "{letter}" в кортеже встречается {count} раз(а)')
