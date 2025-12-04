# Number 1
def sum_of_integers(n):
    # Mathematical formula
    return n * (n + 1) // 2

# Validation for n = 10
n = 10
calculated = sum_of_integers(n)
actual = sum(range(1, n + 1))

print(f"Sum of the first {n} integers: ")
print(f"Formula result: {calculated}, Direct calculation: {actual}")
print("Valid" if calculated == actual else "Not Valid")

# Number 2
def validate_induction_simple(n_max):

    for n in range(1, n_max + 1):
        calculated = n * (n + 1) // 2
        actual = sum(range(1, n + 1))

        if calculated != actual:
            return f"Induction failed at n = {n}"

    return "Induction succeeded for all n up to " + str(n_max)

# Validation up to n = 10
print(validate_induction_simple(10))

# Number 3
def validate_induction_simple(n_max):

    for n in range(1, n_max + 1):
        calculated = n * (n + 1) // 2
        actual = sum(range(1, n + 1))

        if calculated != actual:
            return f"Induction failed at n = {n}"

    return "Induction succeeded for all n up to " + str(n_max)

# Validation up to n = 10
print(validate_induction_simple(10))

# Number 4
def pascal_row_sum(n):

    # Calculating the sum of elements in the n-th row of Pascal's triangle
    return sum(2**i for i in range(n))

# Validation for rows 1 to 10
for n in range(1, 11):
    calculated = pascal_row_sum(n)
    actual = 2**(n - 1)
    print(f"Row {n}: Calculation result = {calculated}, "
          f"Formula = {actual}, Valid = {calculated == actual}")