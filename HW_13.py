# Користувач вводить через дефіс дві літери,
# Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба,
# мінімальне значення завжди менше або дорівнює максимальному.

#text = 'a-c' # -> abc
#text = 'a-a' # -> a
#text = 's-H' #-> stuvwxyzABCDEFGH
#text = 'a-A' #-> abcdefghijklmnopqrstuvwxyzA


import string
ascii_letters = string.ascii_letters

text = input('Type text:  ')
begin = ascii_letters.find(text[0])
end = ascii_letters.find(text[-1])+1
print(ascii_letters[begin: end])