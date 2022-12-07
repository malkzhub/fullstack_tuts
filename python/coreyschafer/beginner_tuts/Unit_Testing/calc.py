
def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x -y

def multiply(x, y):
    """Multiply Function"""
    return x * y
    # return x ** y # AssertionError

def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Cannot be divided by zero!')

    return x / y
    # return x // y # AssertionError - Must update unit testing file


