# Replace the "ANSWER HERE" for your answer hola

def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x>y:
        return x
    else:
        return y

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if (x>y and z<y) or (x>z and y<z):
        return x
    elif (y>x and z<x) or (y>z and x<z):
        return y
    else:
        return z
