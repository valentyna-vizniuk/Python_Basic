# На запит від програми, користувач вводить 5-ти значне ціле, позитивне число.
# Вам необхідно "перевернути" цє число  задом наперед, тобто щоб у результаті
# вийшло теж 5-ти значне число, але із зворотною послідовністю цифр.


x = int(input('Type int: '))
y = x % 10
x = x // 10
z = x % 10
x = x // 10
v = x % 10
x = x // 10
t = x % 10
x = x // 10
o = x % 10
y = y * 10000
z = z * 1000
v = v * 100
t = t *10
n = y+z+v+t+o
print('Inverted type:', n)