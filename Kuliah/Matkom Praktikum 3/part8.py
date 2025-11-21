# Number 1
def f(x):
    return 2 * x + 3

def f_inverse(y):
    return (y - 3) / 2

x = 10
y = f(x)
print("f(x) =", y)
print("f_inverse(y) =", f_inverse(y))

# Number 2
def f(x):
    return x + 2

def g(x):
    return 3 * x

def f_g(x):
    return f(g(x))

x = 4
print("f(g(x)) =", f_g(x))

# Number 3
import math

def identity(x):
    return x

def absolute(x):
    return abs(x)

def floor_value(x):
    return math.floor(x)

def ceil_value(x):
    return math.ceil(x)

x = -3.7
print("Identity(x):", identity(x))
print("Absolute(x):", absolute(x))
print("Floor(x):", floor_value(x))
print("Ceil(x):", ceil_value(x))
#---------------------------------------
def identity(x):
    return x

def constant(c):
    def f(x):
        return c
    return f

def absolute_value(x):
    return abs(x)

x_values = [-10, 0, 10]

print("Identity Function:")
for x in x_values:
    print(f"identity({x}) =", identity(x))

print("\nConstant Function (c = 7):")
constant_func = constant(7)
for x in x_values:
    print(f"constant(7)({x}) =", constant_func(x))

print("\nAbsolute Value Function:")
for x in x_values:
    print(f"absolute_value({x}) =", absolute_value(x))
    
# Number 4
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 9
print("Factorial(n):", factorial(n))
print("Fibonacci(n):", fibonacci(n))

