# 7. Дан список [student1, student2, student3] с помощью цикла for
# добавить к каждому элементу списка слово “_good”. Вывести на экран.

list_students = ['student1', 'student2', 'student3']
for i in range(len(list_students)):
    list_students[i] += '_good'
print(list_students)
