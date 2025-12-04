# Number 1
def is_prime(n):
    """
    Check if a number n is prime.
    A prime number has no divisors other than 1 and itself.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_factorization(n):
    """
    Return the list of prime factors of n using repeated division.
    This shows that every number n >= 2 can be expressed as a product of primes.
    """
    factors = []
    divisor = 2

    while n > 1:
        # If divisor is prime and divides n, record it
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1  # Move to the next possible divisor

    return factors


print("Number | Prime Factorization")
print("-" * 32)

for num in range(10, 31):
    print(f"{num:<6} | {prime_factorization(num)}")


"""
Explanation (Strong Induction):

This program shows that every integer n >= 2
can be broken down into a product of prime numbers.

Strong induction is used to prove this property:

1. Base case:
   n = 2 is prime → can be represented as itself.

2. Induction step:
   Assume every integer from 2 to k can be represented
   as prime factorization.

   For number k+1:
   - If k+1 is prime → it is already a product of primes.
   - If k+1 is composite → it can be written as ab
     where 2 <= a < k+1 and 2 <= b < k+1.
     By the induction hypothesis, a and b both
     have prime factorizations → so does k+1.

Therefore, strong induction confirms that all integers n >= 2
have prime factorization.
"""

# Number 2
def f(n):
    """
    Recursive Fibonacci-like function based on:
    f(1) = 1
    f(2) = 2
    f(n) = f(n-1) + f(n-2), for n >= 3
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    return f(n - 1) + f(n - 2)


def fib(n):
    """
    Iterative version for comparison.
    This computes the same sequence more efficiently.
    """
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2  # initial values for f(1) and f(2)
    for _ in range(3, n + 1):
        a, b = b, a + b  # shift forward
    return b


print("n | Recursive f(n) | Iterative fib(n) | Match?")
print("-" * 45)

for n in range(1, 16):
    recursive_val = f(n)
    iterative_val = fib(n)
    match = "Yes" if recursive_val == iterative_val else "No"
    print(f"{n:2} | {recursive_val:14} | {iterative_val:17} | {match}")


"""
Explanation:

This program verifies that the recursive function definition
follows the Fibonacci pattern, but starting with f(1)=1 and f(2)=2
instead of the usual 1 and 1.

General Induction is used to prove that if the recursion
holds for the previous terms (n-1 and n-2),
then the formula correctly defines all future values.

Matching recursive and iterative results for n=1..15
shows the recursive definition is accurate.
"""
