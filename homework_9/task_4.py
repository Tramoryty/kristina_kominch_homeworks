# 4) На вход программы подается словарь a = {1:10, 2:20, 3:30},
# необходимо получить список произведения ключа на значение.

a = {1: 10, 2: 20, 3: 30}
a_new = []
for key, value in a.items():
    a_new.append(key * value)
print(a_new)
