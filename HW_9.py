# Створіть список випадкових чисел із випадковою
# кількістю елементів від 3 до 10.
# Ваше завдання - створити новий список з 3 елементів
# початкового списку - першим, третім і другим з кінця.

import random
list = []
list = [random.randint(1, 100) for i in range(random.randint(3, 10))]
print(list)
x = list[0]
y = list[2]
z = list[-2]
list2 = [x, y, z]
print(list2)

