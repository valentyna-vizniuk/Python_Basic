# Модифікуйте клас Група (завдання минулої лекції) так,
# щоб при спробі додавання до групи більше 10-ти студентів, було порушено виняток користувача.
# Таким чином потрібно створити ще й виняток користувача для цієї ситуації.
# І обробити його поза межами класу.
# Тобто,потрібно перехопити цей виняток, при спробі додавання 11-го студента.
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


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise MaxStudentdError
        else:
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
st2 = Student('Female', 27, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'Max', 'Macon', 'AN145')
st4 = Student('Male', 25, 'Bob', 'Marly', 'AN145')
st5 = Student('Female', 23, 'Madonna', 'Henes', 'AN145')
st6 = Student('Female', 28, 'Anna', 'Taylor', 'AN145')
st7 = Student('Female', 25, 'Kate', 'Mendeley', 'AN145')
st8 = Student('Male', 25, 'Lucas', 'Sotul', 'AN145')
st9 = Student('Male', 26, 'Sem', 'Knif', 'AN145')
st10 = Student('Male', 29, 'Garry', 'Spir', 'AN145')
st11 = Student('Female', 30, 'Sindiya', 'Lopes', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)

class MaxStudentdError(Exception):
    def __init__(self, message="Досягнуто максимум у групі"):
        super().__init__()
        self.message = message
try:
    gr.add_student(st11)
except MaxStudentdError as err:
    print(err.message)
    print(gr)

