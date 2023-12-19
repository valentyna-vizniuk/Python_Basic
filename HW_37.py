# Створіть клас «Прямокутник», у якого необхідно реалізувати два поля
#     (ширина та висота) та кілька обов'язкових методів:
#     Метод порівняння прямокутників за площею.
#     Метод складання прямокутників (площа сумарного прямокутника повинна
#     дорівнювати сумі площ прямокутників, які ви складаєте).
#     Методи множення прямокутника на число n (це має збільшити площу базового прямокутника в n разів).
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Rectangle):
            new_square = self.get_square() + other.get_square()
            new_width = new_square * 0.5
            return Rectangle(new_width, new_square // new_width)
        return NotImplemented

    def __mul__(self, n):
        new_width = self.width * n
        return Rectangle(new_width, self.height)

    def __str__(self):
        return "Rectangle [width = {}, height = {}".format(self.width, self.height)


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print('OK')