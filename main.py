class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturer_hw(self, lecturer, course, grade): # задание 2
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.l_grades:
                lecturer.l_grades[course] += [grade]
            else:
                lecturer.l_grades[course] = [grade]
        else:
            return 'Ошибка'

    def medium(self):
        for key_med, values_med in self.grades.items():
            return sum(values_med) / len(values_med)

    def __str__(self): # задание 3
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.medium()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other): # задание 3
        if not isinstance(other, Student):
            print('Некорректное сравнение')
            return
        return self.medium() > other.medium()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor): # задание 1 - создали классы Lecturer и Reviewer
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.l_grades = {}

    def medium(self):
        for key_med, values_med in self.l_grades.items():
            return sum(values_med) / len(values_med)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.medium()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Некорректное сравнение')
            return
        return self.medium() > other.medium()

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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


lector = Lecturer('Ivan','Sidorov')
lector.courses_attached += ['Python']
lector2 = Lecturer('Petr' , 'Sokol')
lector2.courses_attached += ['Python']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
normal_student = Student('Artem', "Zopov", "male")
normal_student.courses_in_progress += ['Python']
normal_student.courses_in_progress += ['Git']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
normal_mentor = Reviewer('Jack', 'Tomson' )
normal_mentor.courses_attached += ['Git']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(normal_student, 'Python', 7)
normal_mentor.rate_hw(best_student, 'Git', 10)
normal_mentor.rate_hw(normal_student, 'Git', 7)

best_student.lecturer_hw(lector, 'Python', 10)
best_student.lecturer_hw(lector, 'Python', 9)
best_student.lecturer_hw(lector2, 'Python', 9)



print(lector)
print()
print(best_student)
print()
print(f'Поставим оценки лектору: {lector.l_grades}')
print(f'Средняя оценка лектора: {lector.medium()}')
# print(normal_student.medium())
# print(lector2.medium())
print(f'Оценки у первого лектора лучше чем у второго? - {lector.__lt__(lector2)}')
# print(', '.join(best_student.courses_in_progress))
# print(best_student.courses_in_progress)
# print(best_student.__lt__(normal_student))

student_list = [best_student, normal_student]
student_score = []
def average_rating_stud(stud_list, title): # задание 4
    for a in stud_list:
        for b in a.grades.get(title):
            student_score.append(b)
    return round(((sum(student_score)) / len(student_score)),2)
print(f"Средняя оценка студентов по курсу Python: {average_rating_stud(student_list, 'Python')}")
# print(average_rating_stud(student_list, 'Git'))

lecturer_list = [lector, lector2]
lecturer_score = []
def average_rating_lecturer(lect_list, title): # задание 4
    for a in lect_list:
        for b in a.l_grades.get(title):
            lecturer_score.append(b)
    return round(((sum(lecturer_score)) / len(lecturer_score)), 2)
# print(average_rating_lecturer(lecturer_list, 'Python'))





