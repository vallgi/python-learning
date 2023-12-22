''' a function that takes a number and convert it to radian and convert the radian function to degrees'''


import math 
def my_function():
    num=1
    if num <= 0:
        print ('invalid')
    else:
        print('valid')
my_function()
for num in range(1, 10):
    num += 1
    print(num)
rads = math.radians(num)
print(rads)
deg=math.degrees(rads)
print(deg)

    







import math
def my_function():
    num=1
    if num <= 0:
        print ('invalid')
    else:
        print('valid')
my_function()
for num in range(1, 10):
    num += 1
    print(num)
    rads = math.radians(num)
    print(rads)
    deg=math.degrees(rads)
    print(deg)
