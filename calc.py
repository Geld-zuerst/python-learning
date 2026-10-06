import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


def modulo(a, b):
    if b == 0:
        raise ZeroDivisionError("Modulo by zero is not allowed.")
    return a % b


def square_root(a):
    if a < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    return math.sqrt(a)
