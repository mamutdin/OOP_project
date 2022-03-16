def average(directory):
    summ = 0
    count = 0
    for value in directory.values():
        for mark in value:
            summ += mark
            count += 1
    average_mark = summ / count
    return average_mark


students = []
lecturers = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students.append(self)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecture_grades:
                lecturer.lecture_grades[course] = lecturer.lecture_grades[course] + [grade]
            else:
                lecturer.lecture_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average(self.grades)}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {' '.join(self.finished_courses)}"
        return text

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return average(self.grades) < average(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}
        lecturers.append(self)

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average(self.lecture_grades)}"
        return text

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return average(self.lecture_grades) < average(other.lecture_grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}"
        return text


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

other_student = Student('Other', 'Eman', 'your_gender')
other_student.courses_in_progress += ['Python']
other_student.courses_in_progress += ['Git']
other_student.finished_courses += ['Введение в программирование']

some_mentor = Mentor('Some', 'Buddy')
some_mentor.courses_attached += ['Python']
some_mentor.courses_attached += ['Git']

other_mentor = Mentor('Any', 'One')
other_mentor.courses_attached += ['Python']
other_mentor.courses_attached += ['Git']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

other_reviewer = Reviewer('Any', 'One')
other_reviewer.courses_attached += ['Python']
other_reviewer.courses_attached += ['Git']

some_lecturer = Lecturer('Any', 'One')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

cool_lecturer = Lecturer('Cool', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

some_reviewer.rate_hw(some_student, 'Python', 9)
other_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(other_student, 'Python', 7)
other_reviewer.rate_hw(other_student, 'Git', 9)

some_student.rate_lecture(some_lecturer, 'Python', 6)
other_student.rate_lecture(some_lecturer, 'Python', 7)
some_student.rate_lecture(some_lecturer, 'Git', 9)
other_student.rate_lecture(some_lecturer, 'Git', 8)
some_student.rate_lecture(cool_lecturer, 'Python', 7)
other_student.rate_lecture(cool_lecturer, 'Python', 8)
some_student.rate_lecture(cool_lecturer, 'Git', 10)
other_student.rate_lecture(cool_lecturer, 'Git', 9)

print(some_reviewer)
print()
print(some_lecturer)
print()
print(some_student)
print(some_student < other_student)
print(some_lecturer < cool_lecturer)


# def average_hw(students_list, course):
#     i = 0
#     for student in students_list:
#         if course in student.grades.keys():
#             i += student.grades[course]
#     aver = i/len(students_list)
#     return aver
def average_hw(students_list, course):
    i = 0
    for student in students_list:
        if course in student.grades.keys():
            for grade in student.grades[course]:
                i += grade / len(student.grades[course])
            aver = i / len(students_list)
    return aver


print(average_hw(students, 'Python'))


def average_lecture(lecturers_list, course):
    i = 0
    for lecturer in lecturers_list:
        if course in lecturer.lecture_grades.keys():
            for grade in lecturer.lecture_grades[course]:
                i += grade / len(lecturer.lecture_grades[course])
            aver = i / len(lecturers_list)
    return aver


print(average_lecture(lecturers, 'Python'))
