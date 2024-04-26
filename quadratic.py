import math

def roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"({root1}, {root2})"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"({root})"
    else:
        return "()"

def value_y(a, b, c, x):
    return a * x**2 + b * x + c

def to_string(a, b, c):
    return f"f(x) = {a} * X^2 + {b} * X + {c}"

def derivation(a, b, c):
    derivative_a = 2 * a
    derivative_b = b
    return f"f'(x) = {derivative_a}x + {derivative_b}"
