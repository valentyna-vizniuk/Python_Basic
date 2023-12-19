# Напишіть функцію common_elements, яка згенерує два списки елементів .
# Один список з числами кратними 3, інший з кратними числами 5.
# Кількість елементів у цих списках може бути різним.
# За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
# Функція повинна повернути цю множину як результат своєї роботи.


import random
def common_elements() -> set:
    lst_3 = [random.randrange(3, 150, 3) for el in range(30)]
    lst_5 = [random.randrange(5, 150, 5) for el in range(30)]
    print(lst_3)
    print(lst_5)
    return set(lst_3).intersection(set(lst_5))

print(common_elements())


