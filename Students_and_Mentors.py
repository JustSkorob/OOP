class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        sum_grades = sum(sum(grades) for grades in self.grades.values())
        amount_grades = sum(len(grades) for grades in self.grades.values())
        return sum_grades / amount_grades

    def __str__(self):
        average = self.average_grade()
        return (f'Информация о студенте:\n'
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашнее задание: {average}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершённые курсы: {", ".join(self.finished_courses)}\n')

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lector) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course].append(grade)
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        sum_grades = sum(sum(grades) for grades in self.grades.values())
        amount_grades = sum(len(grades) for grades in self.grades.values())
        return sum_grades / amount_grades

    def __str__(self):
        average = self.average_grade()
        return ('Информация о лекторе:\n'
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {average}\n')

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()


class Reviewer(Mentor):
    def __str__(self):
        return (f'Информация о проверяющем:\n'
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Подсчет средней оценки за домашние задания по всем студентам в рамках курса

def average_hw_grade(student_list, course):
    total_grades = 0
    total_count = 0
    for student in student_list:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_count += len(student.grades[course])
    return total_grades / total_count if total_count != 0 else 0


# Подсчет средней оценки за лекции всех лекторов в рамках курса

def average_lecture_grade(lectors_list, course):
    total_grades = 0
    total_count = 0
    for lector in lectors_list:
        if course in lector.grades:
            total_grades += sum(lector.grades[course])
            total_count += len(lector.grades[course])
    return total_grades / total_count if total_count != 0 else 0


# Создание экземпляров классов

student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_2 = Student('Alice', 'Johnson', 'female')

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_2 = Reviewer('Many', "Pie")

lector_1 = Lector('John', 'Doe')
lector_2 = Lector('Ada', 'Lovelace')

# Присвоение курсов студентам и лекторам

student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ["JS"]

student_2.courses_in_progress += ['JS', 'C++']
student_2.finished_courses += []

reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2.courses_attached += ['JS', 'C++', 'Git']

lector_1.courses_attached += ['Python', 'Git']
lector_2.courses_attached += ['JS', 'Git']

# Оценки студентов и лекторов

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, "Git", 6)

reviewer_2.rate_hw(student_2, 'JS', 7)
reviewer_2.rate_hw(student_2, "C++", 9)

student_1.rate_lector(lector_1, 'Python', 7)
student_1.rate_lector(lector_1, 'Python', 10)
student_1.rate_lector(lector_1, 'Python', 8)

student_1.rate_lector(lector_1, 'Git', 6)
student_1.rate_lector(lector_1, 'Git', 10)
student_1.rate_lector(lector_1, 'Git', 10)

student_2.rate_lector(lector_2, 'JS', 4)
student_2.rate_lector(lector_2, 'JS', 8)


# Вывод информации о созданных объектах

print(reviewer_1)
print(reviewer_2)
print(lector_1)
print(lector_2)
print(student_1)
print(student_2)


# Примеры использования функций

students = [student_1, student_2]
lectors = [lector_1, lector_2]

print(f"Средняя оценка за домашние задания по курсу 'Python': {average_hw_grade(students, 'Python')}")
print(f"Средняя оценка за домашние задания по курсу 'Git': {average_hw_grade(students, 'Git')}")

print(f"Средняя оценка за лекции по курсу 'Python': {average_lecture_grade(lectors, 'Python')}")
print(f"Средняя оценка за лекции по курсу 'Git': {average_lecture_grade(lectors, 'Git')}")

# Сравнение студентов
print('student_1 > student_2:', student_1 > student_2)
print('student_1 < student_2:', student_1 < student_2, '\n')

# Сравнение лекторов
print('lector_1 > lector_2:', lector_1 > lector_2)
print('lector_1 < lector_2:', lector_1 < lector_2)
