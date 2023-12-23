''' sorting a list in acs,dec,none'''


import math

def new_numbers():
    num = input('Enter numbers separeted by spaces: ')

    numbers = [int(x)for x in num.split()]

    acs = sorted(numbers)
    dec=sorted( numbers, reverse = True)
    print(numbers)
    print(acs)  
    print(dec)  
new_numbers()





