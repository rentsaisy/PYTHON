# Number 1
def sum_list(L):
    """
    Manually calculate the sum of all elements
    in the list L using a loop.
    """
    total = 0                     # Start with zero
    for value in L:               # Loop through each element of the list
        total += value            # Add each element to the total
    return total                  # Return the final sum


# Example list provided in the task
L = [2, 5, 7, 10]

# Calculate sum with custom function
manual_sum = sum_list(L)

# Compare with Python's built-in sum()
builtin_sum = sum(L)

print("List:", L)
print("Sum using sum_list():", manual_sum)
print("Sum using built-in sum():", builtin_sum)

"""
Comment:
The results are the same, showing that our manual summation
algorithm works correctly. The built-in sum() is faster
and already optimized in Python, but understanding the manual
process is important for learning algorithm basics.
"""

# Number 2
# Pseudocode:
# Algorithm Find_Max(L)
# 1. Start
# 2. Set max_value = L[0]
# 3. For each element x in L starting from the second element:
#        If x > max_value:
#             Set max_value = x
# 4. Return max_value
# 5. End

def find_max(L):
    """
    Find the maximum value in the list L manually
    without using built-in max() function.
    """
    max_value = L[0]  # Assume first element is the maximum initially
    
    # Check the rest of the elements
    for x in L[1:]:
        if x > max_value:
            max_value = x  # Update maximum
    
    return max_value


# Test data
L = [4, 1, 6, 9, 3]

# Test function
manual_max = find_max(L)
builtin_max = max(L)  # For comparison only

print("List:", L)
print("Maximum using find_max():", manual_max)
print("Maximum using built-in max():", builtin_max)

"""
Comment:
Both results match, which confirms that our algorithm correctly
finds the maximum value in a list. The manual process is useful
for understanding algorithmic thinking before relying on built-in
functions like max() in Python.
"""

# Number 3
def linear_search(L, x):
    """
    Perform linear search to find the value x in list L.
    Returns the index if found, otherwise returns -1.
    """
    for i in range(len(L)):        # Loop through indexes 0 to len(L)-1
        if L[i] == x:              # Check if current element matches x
            return i               # Return index where x is found
    return -1                      # x not found in the list


# Test data
L = [10, 20, 30, 40, 50]

# Test 1: x = 30 (expected to be found)
x1 = 30
result1 = linear_search(L, x1)
if result1 != -1:
    print(f"{x1} found at index {result1}")
else:
    print(f"{x1} not found in the list")

# Test 2: x = 45 (expected NOT found)
x2 = 45
result2 = linear_search(L, x2)
if result2 != -1:
    print(f"{x2} found at index {result2}")
else:
    print(f"{x2} not found in the list")

"""
Comment:
Linear search checks each element one by one
from the beginning of the list to the end.

If the element is found → return the index.
If the loop finishes without finding a match → return -1.

This algorithm is simple and works well for small lists,
but it is slower for large lists compared to algorithms such as binary search.
"""

# Number 4
def gcd_subtraction(a, b):
    """
    Find GCD (Greatest Common Divisor) using subtraction method.
    This repeatedly subtracts the smaller number from the larger one.
    """
    while a != b:     # Continue until both numbers become equal
        if a > b:
            a = a - b  # Reduce a
        else:
            b = b - a  # Reduce b
    return a  # or return b (both are equal)


# Test examples from the task
pairs = [(48, 18), (56, 42), (100, 75)]

for x, y in pairs:
    result = gcd_subtraction(x, y)
    print(f"GCD of ({x}, {y}) = {result}")


"""
Comment:
The subtraction method is correct but slower for large numbers.
The Euclidean division-based GCD algorithm:

    while b != 0:
        a, b = b, a % b
    return a

is faster because modulus (%) reduces the number more quickly.

However, the subtraction-based algorithm helps understand
the idea that GCD is based on reducing numbers step-by-step.
"""