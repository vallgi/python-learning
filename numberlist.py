num= [1,2,3,4,5,8,7,6]
course = ['history','math','physics','course']
print(num)
print(course)
course.sort()
print(course)
course.sort(reverse=True)
num.sort(reverse=True)
print(course)
print(num)
num.sort()

print(num)
print(max(num))
print(min(num))
print(sum(num))
sorted_course=sorted(course)
print(sorted_course)
print(course.index('course'))
print('art' in course)
for items in course:
    print(items) 
for index, course in enumerate (course):
    print(index, course)  
course_str= ','.join(course)
print(course_str)

