# Написати програму, яка просить користувача ввести 4-х значне число з клавіатури, після чого друкує на екрані стовпчик цифр, з якого це число складається. Наприклад, користувач вводить 1234, а програма виводить:
#
# 1
#
# 2
#
# 3
#
# 4


x = int(input('Type int: '))
y = 1000
left, right = divmod(x, y)
print(left)
print(int(right/100))
print(int((right%100-right%10)/10))
print(int(right%10))

