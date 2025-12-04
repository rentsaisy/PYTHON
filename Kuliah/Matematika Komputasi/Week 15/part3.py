# Number 1
# "Function to check whether a number is prime"

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#################################################
# "Function to factorize an integer n into prime numbers."

def factorize(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        divisor += 1
    return factors

for n in range(2, 21):
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} can be factorized as {factorize(n)}.")

# Number 2
"Hcalculating the sum of squares using a formula"
def sum_of_squares_formula(n):
    return n * (n + 1) * (2 * n + 1) // 6


"Calculating the sum of squares directly"
def sum_of_squares_direct(n):
    return sum(i**2 for i in range(1, n + 1))

# Induction Verification

print("n  |  Formula  |  Direct Calculation  |  Match?")
print("-" * 45)

for n in range(1, 11):
    formula = sum_of_squares_formula(n)
    direct = sum_of_squares_direct(n)
    print(f"{n:3} | {formula:11} | {direct:20} | {'Yes' if formula == direct else 'No'}")