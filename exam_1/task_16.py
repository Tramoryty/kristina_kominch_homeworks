# 16*.
# Дезоксирибонуклеиновая кислота (ДНК) представляет собой
# химическое вещество, находящееся в ядре клеток и несущее
# «инструкции» по развитию и функционированию живых организмов.
# В цепочках ДНК символы «А» и «Т» дополняют друг друга, как «С» и
# «G».Вам нужно вернуть другую дополнительную сторону. Нить
# ДНК никогда не бывает пустой или ДНК вообще не существует.
# Пример: (ввод --> вывод)
#
# “АТТGС" --> "ТААСG"
# “GТАТ" --> "САТА"

dna_helix = input('Введите спираль ДНК: ').upper()
dna_helix_complementary = ''
for letter in dna_helix:
    if letter == 'A':
        dna_helix_complementary += 'T'
    elif letter == 'T':
        dna_helix_complementary += 'A'
    elif letter == 'C':
        dna_helix_complementary += 'G'
    elif letter == 'G':
        dna_helix_complementary += 'C'
print(f'Комплементарная спираль ДНК: {dna_helix_complementary}')
