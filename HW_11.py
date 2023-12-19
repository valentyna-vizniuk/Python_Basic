# Модифікувати калькулятор таким чином,
# щоб він працював доти, доки користувач цього хоче
# Тобто, потрібно робити запит до користувача на продовження
# роботи калькулятора після кожного обчислення -
# якщо користувач ввів yes (можна просто y),
# то нове обчислення, інакше - закінчення роботи.

answ = 'yes'
while answ == 'yes':
    number1 = int(input("Enter first number: "))
    oper = input('Select an operation (Enter +, -, * or / ): ')
    number2 = int(input("Enter second number: "))

    if oper == '+':
        result = number1 + number2
        print(result)
    elif oper == '-':
        result = number1 - number2
        print(result)
    elif oper == '*':
        result = number1 * number2
        print(result)
    elif oper == '/':
        if number2 != 0:
            result = number1 / number2
            print(result)
        else:
            print('Division by zero!')
    else:
        print('Bad action!')
    answ = input('Сontinue? yes/not ').lower()
