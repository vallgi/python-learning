students = ['math','english','swahili','science']
print(students)
students.sort()
print(students)
student_new_subjects= ['compsci','social studies','cre','chem']
students.insert(0,student_new_subjects)
print(students)
students.extend(student_new_subjects)
print(students)
students.remove('chem')
print(students)
students.pop()
print(students)
popped=students.pop()
print(popped)
students.reverse()
print(students)
