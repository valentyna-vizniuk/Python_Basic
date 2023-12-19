# Ваше завдання — написати програму,
# яка переводить число у формат часу у читальному вигляді.
# Користувач повинен ввести число більше або дорівнює 0 і менше ніж 8640000.
# Число, яке є кількістю секунд, необхідно перевести в дні,
# години, хвилини та секунди.
# Ну і додатковим завданням є турбота про виведення.
# Слово "день" підбирається на основі кількості днів,
# а години, хвилини і секунди повинні заповнюватися нулями при одноцифрових значеннях.

digit = int(input('Type seconds: '))
if 0 <= digit < 8640000:
    days, digit = divmod(digit, 24*60*60)
    hours, digit = divmod(digit, 60*60)
    minut, sec = divmod(digit, 60)
    days = str(days)
    hours = str(hours).zfill(2)
    minut = str(minut).zfill(2)
    sec = str(sec).zfill(2)
    if 5 < int(days) < 21:
        day_str = 'днів'
    elif days[-1] == '1':
        day_str = 'день'
    elif days[-1] in '234':
        day_str = 'дні'
    else:
        day_str = 'днів'
    print(f'{days} {day_str}, {hours}:{minut}:{sec}')
else:
    print('Bad data')