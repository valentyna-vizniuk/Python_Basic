# Ваше завдання — написати програму,
# яка перемножує всі цифри, введені користувачем цілого числа,
# поки воно не стане менше або дорівнювати 9.
# Користувач вводить число з клавіатури.

# 1000 #-> 0
# 423 #-> 8
# 33 #-> 9
# 25 #-> 0
# 1 #-> 1

digit = input('Type digit: ')
while len(digit) > 1:
    tmp = 1
    for d in digit:
        tmp *= int(d)
    digit = str(tmp)
print(digit)