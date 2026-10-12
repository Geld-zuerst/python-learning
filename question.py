import math

def area(a, b, shape):
    if shape == "Square":
        if a == b:
            print(a*a)
        else:
            print("Square should be equal sides")
    elif shape == "rectangle":
        print(a*b)
    elif shape == "circle":
        print((22 / 7)*a**2)
    else:
        print("Please give valid attributes")

def triangle():
    a = int(input("Enter first side: "))
    b = int(input("Enter second side: "))
    c = int(input("Enter third side: "))

    s = (a + b + c) / 2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print(area)


def temperature_change(initial_temp, final_temp):
    initial_fahrenheit = (initial_temp * 9 / 5) + 32
    final_fahrenheit = (final_temp * 9 / 5) + 32
    print(f"Initial temperature in Fahrenheit: {initial_fahrenheit}°F")
    print(f"Final temperature in Fahrenheit: {final_fahrenheit}°F")



temperature_change(30, 45)

# surface, Volume, CSF, and Groung Surface area
# Cuboid
# Cylinder
# Cone