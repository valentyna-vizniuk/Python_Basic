# Користувач вводить рядок.
# Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може:
#     починатися з цифри,
#     складатися тільки з цифр,
#     містити великі літери, пропуск і знаки пунктуації
#     (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
#     бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної може складатися тільки з одного нижнього підкреслення "_".
# Список зареєстрованих слів можна взяти із keyword.kwlist.
# У результаті перевірки на друк виводиться або True,
# якщо таке ім'я змінної допустимо, або False - якщо ні.
# Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно)

# txt = '_' #=> True
# txt = 'x' #=> True
# txt = 'get_value' #=> True
# txt = 'get value' #=> False
# txt = 'get!value' #=> False
# txt = 'some_super_puper_value' #=> True
# txt = 'Get_value' #=> False
# txt = 'get_Value' #=> False
# txt = 'getValue' #=> False
# txt = '3m' #=> False
# txt = 'm3' #=> True
# txt =' assert '#=> False

import string
import keyword
name = input('Type name: ')
res = True
punct = string.punctuation.replace('_', " ")
if name[0].isdigit():
    res = False
elif name in keyword.kwlist:
    res = False
for c in punct:
    if c in name:
        res = False
        break
if name != '_':
    if not name.islower():
        res = False
print(res)