"""
greet users when they log into the system
"""

def greet(username):
    """
    a function to greet a user when they log into the learning platform
    username: the name of the user logging into the platform
    """
    print(f"Hello, world {username}")
    print(f"How do you do {username}")
    print(f"Its nice to learn python with {username}")

greet("Violet")
greet("Dennis")
greet("Brenda")
greet("Ken")


def add(num1=50, num2=30):
    if type(num1) != int or type(num2) != int:
        print("Invalid first number or second number")
    else:
        sum = num1 + num2
        print(f"{num1} + {num2} = {sum}!")

add()
add(40, 70)
add(60, 90)
add(50, 50)