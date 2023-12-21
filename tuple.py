tuple_1=('history','math','physics','comp sci')
tuple_2= tuple_1
print(tuple_1)
print(tuple_2)

cs_course={'history','math','physics','comp sci'}
print(cs_course)
print('math' in cs_course)
art_course={'history','math','art','design'}
print(cs_course.intersection(art_course))
print(cs_course.union(art_course))
print(cs_course.difference(art_course))
empty_list=[]
