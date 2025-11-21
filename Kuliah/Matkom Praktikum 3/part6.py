# Number 1
# Defining the set A and relation R
A = {1, 2, 3}
R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3)}

# Check the reflexive property
is_reflexive = all((a, a) in R for a in A)

# Check the antisymmetric property:
is_antisymmetric = all((b, a) not in R for (a, b) in R if a != b)

# Check the transitive property:
is_transitive = all(
    (a, c) in R
    for (a, b) in R
    for (b2, c) in R
    if b == b2
)

# Determine whether R is a partial order relation
is_partial_order = is_reflexive and is_antisymmetric and is_transitive

print("Is R a partial order relation?", is_partial_order)

# Number 2
import numpy as np

# Define the set A and the relation R
A = {1, 2, 3}
R = {(1, 2), (2, 3)}

# Create the adjacency matrix
size = len(A)
adj_matrix = np.zeros((size, size), dtype=int)

# Create a mapping from element -> index (for matrix positions)
index_map = {value: index for index, value in enumerate(A)}

# Fill the adjacency matrix based on relation R
for (a, b) in R:
    adj_matrix[index_map[a]][index_map[b]] = 1

# Apply the Warshall Algorithm to compute the transitive closure
for k in range(size):
    for i in range(size):
        for j in range(size):
            adj_matrix[i][j] = adj_matrix[i][j] or (adj_matrix[i][k] and adj_matrix[k][j])

print("Transitive Closure Matrix:\n", adj_matrix)

# Number 3
# Defining a 3-ary relation R (student, subject, score)
R = [("Deny", "Mathematics", 90),
     ("Bob", "Science", 85)]

# Display each element in R
for student, subject, score in R:
    print(f"Student: {student}, Subject: {subject}, Score: {score}")

# Number 4
# Defining the sets A and B, and the function f
A = {1, 2, 3}
B = {4, 5, 6}
f = {(1, 4), (2, 5), (3, 6)}

# Check if f is a function:
# A function must map each element of A to exactly one element of B
is_function = len(f) == len(A)

# Check injectivity (one-to-one):
# No two different elements in A map to the same element in B
is_injective = len({b for (_, b) in f}) == len(f)

# Check surjectivity (onto):
# Every element of B must appear as an output in f
is_surjective = {b for (_, b) in f} == B

print("Is f a function? :", is_function)
print("Is f injective? :", is_injective)
print("Is f surjective? :", is_surjective)
