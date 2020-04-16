grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}


def students_names(class_name):
        a = input('class_name: ')
        if a == 'grade_one':
            return list(grade_one.keys())
        elif a == 'grade_two':
            return list(grade_two.keys())
        elif a == 'grade_three':
            return list(grade_three.keys())

def student_score(class_name, student_name):
    b = input('class_name: ')
    c = input('student_name: ')
    if b == 'grade_one':
        return sum(grade_one.get(c))
    if b == 'grade_two':
        return sum(grade_two.get(c))
    if b == 'grade_three':
        return sum(grade_three.get(c))

def students_count(class_name):
        d = input('class_name: ')
        if d == 'grade_one':
            return len(list(grade_one.keys()))
        elif d == 'grade_two':
            return len(list(grade_two.keys()))
        elif d == 'grade_three':
            return len(list(grade_three.keys()))

print('Choose one: students_names, student_score, students_count')

choice = input()

if choice == 'students_names':
    print(students_names('class_name'))

if choice == 'student_score':
    print(student_score('class_name', 'student_name'))

if choice == 'students_count':
    print(students_count('class_name'))

x = input("if finished, type 'done' or type 'more' to do another function: ")

while  x =='more':
    print('Choose one: students_names, student_score, students_count')

    choice = input()

    if choice == 'students_names':
        print(students_names('class_name'))

    if choice == 'student_score':
        print(student_score('class_name', 'student_name'))

    if choice == 'students_count':
        print(students_count('class_name'))

    x = input("if finished, type 'done' or type 'more' to do another function: ")


    if x == 'done':
        break
