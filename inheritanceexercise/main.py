class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def __str__(self):
        return f'{self.name}({self.address})'


class Student(Person):
    numCourses = 0
    courses = []
    grades = []

    def __init__(self, name, address):
        super().__init__(name, address)

    def addCourseGrade(self, course:str, grade:int):
        if course not in self.courses:
            self.courses.append(course)
            self.grades.append(grade)
        else:
            self.grades.append(grade)
        self.numCourses += 1

    def printGrades(self):
        for i in range(len(self.courses)):
            print(f'{self.courses[i]}: {self.grades[i]}')

    def getAverageGrade(self):
        average = sum(self.grades) / self.numCourses
        return average

    def __str__(self):
        return f'Student: {super().__str__()}'

class Teacher(Person):
    numCourses = 0
    courses = []

    def __init__(self, name, address):
        super().__init__(name, address)

    def __str__(self):
        return f'Teacher: {super().__str__()}'

    def addCourse(self, course):
        if course not in self.courses:
            self.courses.append(course)
            self.numCourses += 1
        else:
            return False

    def removeCourse(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            return False


def teacher_page():
    for_input = input('Do you have an account yet?(Yes/No): ')
    if for_input == 'No':
        name = input('Your name: ')
        address = input('Your address: ')
        teacher = Teacher(name=name, address=address)
        teacher_list.append(name)
        print(teacher.__str__())
        teacher_service(teacher)
    if for_input == 'Yes':
        print('Fill in the data below')
        teacher_name = input('Your name: ')
        if teacher_name in teacher_list:
            print(f'Welcome {teacher_name}')
            teacher_service(teacher)

def teacher_service(teacher):
    print('What are you trying to do today?')
    print('1. Add course''\n''2. Remove course')
    inputs = input('Your choice(1/2): ')
    if inputs == '1':
        course_name = str(input("Course: "))
        teacher.addCourse(course=course_name)
        print('Number of course: ', teacher.numCourses)
        answer = input('Do you want to do another action?(Yes/No): ')
        if answer == 'Yes':
            teacher_service(teacher)
        if answer == 'No':
            main()
    if inputs == '2':
        del_course = str(input('Course: '))
        teacher.removeCourse(course=del_course)
        print('Current list of courses: ', teacher.courses)
        answer = input('Do you want to do another action?(Yes/No): ')
        if answer == 'Yes':
            teacher_service(teacher)
        if answer == 'No':
            main()

def student_page():
    for_input = input('Do you have an account yet?(Yes/No): ')
    if for_input == 'No':
        name = input('Your name: ')
        address = input('Your address: ')
        student = Student(name=name, address=address)
        student_list.append(student)
        print(student.__str__())
        student_service(student)
    if for_input == 'Yes':
        print('Fill in the data below')
        student_name = input('Your name: ')
        if student_name in student_list:
            print(f'Welcome {student_name}')
            student_service(student)



def student_service(student):
    print('What are you trying to do today?')
    print('1. Add course and grade''\n''2. Print grades''\n''3. Average grade')
    inputs = input('Your choice(1/2/3): ')
    if inputs == '1':
        course = input('Course: ')
        grade = int(input('Grade: '))
        student.addCourseGrade(course=course, grade=grade)
        print('Collection of courses: ', student.courses)
        print('Collection of grades: ', student.grades)
        answer = input('Do you want to do another action?(Yes/No): ')
        if answer == 'Yes':
            student_service(student)
        if answer == 'No':
            main()
    if inputs == '2':
        print('All of your grades: ')
        student.printGrades()
        answer = input('Do you want to do another action?(Yes/No): ')
        if answer == 'Yes':
            student_service(student)
        if answer == 'No':
            main()
    if inputs == '3':
        print('Your average grade: ', student.getAverageGrade())
        answer = input('Do you want to do another action?(Yes/No): ')
        if answer == 'Yes':
            student_service(student)
        if answer == 'No':
            main()


def main():
    print('Welcome to School!')
    for_input = input("Are you a 'Teacher' or a 'Student': ")
    if for_input == 'Teacher':
        print('Welcome to Teacher Page!')
        teacher_page()
    elif for_input == 'Student':
        print('Welcome to Student Page!')
        student_page()

    else:
        main()

if __name__ == '__main__':
    teacher_list = []
    student_list = []
    main()
