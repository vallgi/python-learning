''' trying to advance or using another loop method to print the same values in task1.py'''


import math 

def my_function():
    num = [1,2,3,4,5,6,7,8,9,10]
    print(sum(num))
    print(max(num))
    print(min(num))
    print(num)
    for items in num:
        
        while items <= 10:
            print(items)
            rads = math.radians(items)
            sine =math.sin(items)
            degs =math.degrees(rads)
            sine1 =math.sin(rads)
            print (f"degrees:{degs}")
            print (f"sin:{sine1}")
            print(f"radians:{rads}")
            print(f"sin:{sine}")
            items += 1
my_function()
