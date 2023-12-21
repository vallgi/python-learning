student={'name':'john','age':25,'course':['math','comp sci']}
print(student)
print(student.get('phone'))
student['phone']=333333
student['name']='jane'
print(student)
del student ['age']
print(student)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())
for keys in student:
    print(keys)
for keys, values in student.items():
     print(keys, values)