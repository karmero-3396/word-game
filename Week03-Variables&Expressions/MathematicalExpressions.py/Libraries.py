import math

def calculate_circle_area(radius) -> float: 
    """Calculate the area of a circle given its radius."""
    return math.pi * radius ** 2

def calculate_hypotenuse(a, b) -> float:
    """Calculate the hypotenuse of a right triangle given the lengths of the other two sides."""
    return math.sqrt(a**2 + b**2)

def calculate_logarithm(value, base=10) -> float:
    """Calculate the logarithm of a value with a specified base (default is 10)."""
    return math.log(value, base)

def calculate_exponential(value) -> float:
    """Calculate the exponential of a value (e^value)."""
    return math.exp(value)

def calculate_sine(angle_in_radians) -> float:
    """Calculate the sine of an angle given in radians."""
    return math.sin(angle_in_radians)

def calculate_factorial(n) -> int:
    """Calculate the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)

def calculate_power(base, exponent) -> float:
    """Calculate the power of a base raised to an exponent."""
    return math.pow(base, exponent)

def calculate_square_root(value) -> float:
    """Calculate the square root of a non-negative value."""
    if value < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    return math.sqrt(value)
