# Програма має виконувати прості математичні дії (+, -, *, /).
# Користувачеві пропонується почерзі ввести числа та дію над цими числами,
# а програма, виходячи з дії, обчислює та друкує результат.


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
oper = input('Select an operation (Enter +, -, * or / ): ')
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
    print('Incorrect data')