# Number 1
# Determine the inverse of a function represented as a dictionary
def inverse_function(A, f):
    # f is a dict mapping x -> f(x)
    inverse_f = {}

    # Swap keys and values to get the inverse mapping
    for x in A:
        y = f[x]
        inverse_f[y] = x  # store f⁻¹(y) = x

    return inverse_f


# Build the function f(x) = 2x + 1 over A
A = {1, 2, 3, 4}
f = {x: 2*x + 1 for x in A}

# Compute its inverse
inv_f = inverse_function(A, f)

# Display the pairs of f and f⁻¹
print("f =", set((x, f[x]) for x in A))
print("f_inverse =", set((y, inv_f[y]) for y in inv_f))

# Number 2
# Define f(x) = 2x + 3
def f(x):
    return 2*x + 3

# Define g(x) = x^2
def g(x):
    return x**2

# Composition function: compute f(g(x))
def compose(f, g, x):
    # First apply g to x, then f to the result
    return f(g(x))

# Test values
values = [1, 2, 3]

print("Results for (f ∘ g)(x):")
for x in values:
    print(x, "->", compose(f, g, x))

print("\nResults for (g ∘ f)(x):")
for x in values:
    # Now compute g(f(x))
    print(x, "->", g(f(x)))
    
# Number 3
# Identity function: returns the input unchanged
def identity(x):
    return x

# Constant function: always returns the same value c
def constant(x, c=5):
    return c

# Linear function: f(x) = a*x + b
def linear(x, a=2, b=1):
    return a*x + b

# Quadratic function: f(x) = a*x^2 + b*x + c
def quadratic(x, a=1, b=0, c=0):
    return a*x**2 + b*x + c


# Display function values for x = -3 to 3
def display_table(func, *params):
    print("x\tf(x)")
    print("----------------")
    for x in range(-3, 4):
        print(f"{x}\t{func(x, *params) if params else func(x)}")

# Demonstrations
print("Identity function:")
display_table(identity)

print("\nConstant function (c = 5):")
display_table(constant, 5)

print("\nLinear function (a = 2, b = 1):")
display_table(linear, 2, 1)

print("\nQuadratic function (a = 1, b = -1, c = -2):")
display_table(quadratic, 1, -1, -2)

# Number 4
# Identity function: returns the input x exactly
def identity(x):
    return x

# Constant function: always returns the same fixed value c
def constant(x, c=5):
    return c

# Linear function: f(x) = a*x + b
# The parameters a and b control slope and vertical shift
def linear(x, a=1, b=0):
    return a*x + b

# Quadratic function: f(x) = a*x^2 + b*x + c
# The parameter a controls curvature, b the tilt, c the vertical shift
def quadratic(x, a=1, b=0, c=0):
    return a*x**2 + b*x + c


# Function to display x and f(x) values in table form
def display_table(func, *params):
    print("x\tf(x)")
    print("----------------")
    for x in range(-3, 4):
        # If the function has additional parameters (a, b, c), pass them
        print(f"{x}\t{func(x, *params) if params else func(x)}")
    print()


# Test outputs for each type of function
print("Identity function:")
display_table(identity)

print("Constant function (c = 5):")
display_table(constant, 5)

print("Linear function (a = 2, b = -1):")
display_table(linear, 2, -1)

print("Quadratic function (a = 1, b = -2, c = -3):")
display_table(quadratic, 1, -2, -3)