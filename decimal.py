''' conversion of decimal to binary'''


def nee_decimal():
    number= input('enter numbers: ')

    new_number= [float(x) for x in number.split()]
    new = [bin(int(y)) for y in new_number]
    print(f"the new number is{new_number} is :{new}")
    print (new_number)
nee_decimal()