# У цьому завданні Вам необхідно зробити дві речі на підставі попереднього ДЗ.
# До класу Студента необхідно додати метод порівняння.
# Порівнювати можна за тими рядками, які повертає метод __str__
# Для того, щоб спрацювала коректно ось ця перевірка
# Рознесіть класи, які використовували під час виконання завдання про групу студентів за модулями.
# Переконайтеся у працездатності проекту –
# створіть окремо файл main.py, у якому необхідно імпортувати потрібні класи та запустити код перевірки.
class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student: {super().__str__()}, {self.record_book}'

    def __eq__(self, other):
        if isinstance(other, Student):
            return (
                self.first_name == other.first_name
                and self.last_name == other.last_name
                and self.record_book == other.record_book
            )
        return NotImplemented

    def __hash__(self):
        return hash((self.gender, self.age, self.first_name, self.last_name, self.record_book))

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete is not None:
            self.group.remove(student_to_delete)
            return student_to_delete
        return None

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += f'{str(student)}\n'
        return f'Number: {self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)

assert gr.find_student('Jobs') == st1, 'Test1'
assert gr.find_student('Jobs2') is None

print(st1 == st2)

gr.delete_student('Taylor')
print(gr) # Only one student

print(st1 == st2)
