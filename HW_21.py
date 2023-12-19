# Ваше завдання – написати функцію is_palindrome,
# яка перевірятиме, чи є рядок паліндромом.
# Паліндромом - це такий рядок,
# який читається однаково зліва направо і зправа наліво
# без урахування знаків пунктуації та розмірності букв.
# Функція приймає на вхід рядок, та повертає булеве значення True або False

def is_palindrome(text) -> bool:
    # tmp = ''.join(c for c in text if c.isalnum()).lower()
    # return tmp == tmp[::-1]
    tmp = ''
    for c in text:
        if c.isalnum():
            tmp += c.lower()
    return tmp == tmp[::-1]

# test
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

assert is_palindrome('0P') == False, 'Test2'