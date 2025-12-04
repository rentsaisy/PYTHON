# Number 1
def sum_odd(n):
    """
    Calculate the sum of the first n odd numbers.
    Example: n = 3 → 1 + 3 + 5 = 9
    """
    total = 0
    odd_number = 1

    for _ in range(n):
        total += odd_number      # Add the current odd number
        odd_number += 2          # Move to the next odd number (odd numbers increase by 2)
    
    return total


# Test the function with sample values
test_values = [3, 6, 10]

print("n  |  Sum of odd numbers  |  n^2  |  Match?")
print("-" * 45)

for n in test_values:
    odd_sum = sum_odd(n)
    square_value = n ** 2
    matches = "Yes" if odd_sum == square_value else "No"
    print(f"{n:2} | {odd_sum:20} | {square_value:4} | {matches}")
    

"""
Explanation:
This program proves the mathematical statement:
The sum of the first n odd integers equals n².

This concept is commonly used in integer number theory,
especially when connecting number patterns with algebraic forms.
It also supports learning about mathematical induction.
"""

# Number 2
def check_inequality(n):
    """
    Check whether the inequality 2^n >= n + 1 holds for a given n.
    Returns True if the statement is correct, otherwise False.
    """
    return 2**n >= n + 1


# Test the inequality for n = 1 to 15
valid_n = []
invalid_n = []

for n in range(1, 16):
    if check_inequality(n):
        valid_n.append(n)    # Record n that satisfies the inequality
    else:
        invalid_n.append(n)  # Record n that does NOT satisfy the inequality


# Display results
print("Values of n that satisfy the inequality 2^n >= n + 1:")
print(valid_n)

print("\nValues of n that do NOT satisfy the inequality (if any):")
print(invalid_n)


"""
Explanation:

This program verifies the mathematical statement
'2^n >= n + 1' using computational checking.

The result shows that the inequality holds for all
tested values (n = 1 to 15). This supports the statement
as a true property for positive integers.

This type of statement is commonly proven using
the Mathematical Induction Principle.
"""

# Number 3
def generate_b(n):
    """
    Generate the nth value of the sequence using the recursive rule:
    b1 = 5
    b(n+1) = b(n) + 4
    """
    b = 5  # initial value b1
    for _ in range(1, n):
        b += 4  # add 4 to get the next term
    return b


def check_b_formula(n):
    """
    Check whether the formula b(n) = 4n + 1
    matches the recursive sequence value.
    """
    return 4*n + 1


print("n | Recursive b(n) | Formula 4n+1 | Match?")
print("-" * 40)

for n in range(1, 13):
    recursive_val = generate_b(n)     # value from recursion
    formula_val = check_b_formula(n)  # value from formula
    match = "Yes" if recursive_val == formula_val else "No"
    print(f"{n:2} | {recursive_val:14} | {formula_val:12} | {match}")


"""
Explanation:
The recursive definition increases each term by +4.
The closed form (explicit formula) b(n) = 4n + 1
comes from repeatedly applying this recursive rule.

Extended (or strong) induction reinforces the idea that
if the formula works for one term and the relation holds,
then it must work for all subsequent terms of the sequence.
"""