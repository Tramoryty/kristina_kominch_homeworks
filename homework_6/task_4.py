# 8)Необходимо с помощью цикла while вывести данную последовательность чисел:
# 1 2 4 16 32 64 128 256 512

i = 1
print(i)
while i < 512:
    i *= 2
    if i == 8:
        continue
    print(i)
