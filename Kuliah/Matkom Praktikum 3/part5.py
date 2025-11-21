# Number 1
# Function to compute the inverse of a relation
def inverse_relation(R):
    # Initialize an empty set to hold the inverse relation
    R_inverse = set()
    # Loop over each pair (a, b) in the original relation R
    for a, b in R:
        # Swap the pair to (b, a) and add to R_inverse
        R_inverse.add((b, a))
    # Return the inverse relation
    return R_inverse

# Define the original relation R
R = {(1, 2), (2, 3), (3, 4), (4, 5)}
# Calculate the inverse relation
R_inv = inverse_relation(R)
# Display the inverse relation
print("Inverse of R:", R_inv)

# Test with another relation
another_relation = {('a', 'b'), ('b', 'c'), ('c', 'd')}
# Calculate the inverse of the new relation
inverse_another_relation = inverse_relation(another_relation)
# Display the result
print("Inverse of the other relation:", inverse_another_relation)

# Number 2
# Function to combine two relations R1 and R2
def combine_relations(R1, R2):
    # Use the union operator to combine the two sets of relations
    combined_relation = R1.union(R2)
    # Return the combined relation set
    return combined_relation

# Define the first relation R1
R1 = {(1, 2), (2, 3), (3, 4)}
# Define the second relation R2
R2 = {(3, 5), (4, 6)}

# Call the function to combine R1 and R2
combined_relation = combine_relations(R1, R2)
# Display the combined relation set
print("Combined relation:", combined_relation)

# Number 3
def compose_relations(R, S):
    # Initialize an empty set to store the composed relation
    composition = set()

    # Loop through each pair (a, b) in relation R
    for (a, b) in R:
        # For each such pair, check all pairs (b2, c) in relation S
        for (b2, c) in S:
            # If the intermediate element matches (b == b2), add (a, c) to the result
            if b == b2:
                composition.add((a, c))
    # Return the composed relation as a set of pairs
    return composition

# Define relation R
R = {(1, 2), (2, 3), (3, 4)}
# Define relation S
S = {(2, 5), (3, 6), (4, 7)}

# Calculate the composition S ∘ R
S_comp_R = compose_relations(R, S)
# Display the result of the composition
print("S ∘ R =", S_comp_R)

# Number 4
def check_relation_properties(A, R):
    # Check if R is reflexive: For all a in A, (a, a) must be in R
    is_reflexive = all((a, a) in R for a in A)
    
    # Check if R is symmetric: For all (a, b) in R, (b, a) must be in R
    is_symmetric = all((b, a) in R for (a, b) in R)
    
    # Check if R is antisymmetric: For all (a, b) in R, if a != b then (b, a) must NOT be in R
    is_antisymmetric = all((a != b) or ((b, a) not in R) for (a, b) in R)
    
    # Check if R is transitive: For all (a, b) and (b, c) in R, (a, c) must be in R
    is_transitive = True
    for (a, b) in R:
        for (b2, c) in R:
            if b == b2:
                if (a, c) not in R:
                    is_transitive = False
                    break
        if not is_transitive:
            break

    # Print the results
    print("Reflexive:", is_reflexive)
    print("Symmetric:", is_symmetric)
    print("Antisymmetric:", is_antisymmetric)
    print("Transitive:", is_transitive)

# Define the set A and relation R
A = {1, 2, 3}
R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}

# Check relation properties
check_relation_properties(A, R)

# Number 5
def check_relation_properties(A, R):
    # Check if R is reflexive: For all a in A, (a, a) must be in R
    is_reflexive = all((a, a) in R for a in A)
    
    # Check if R is symmetric: For all (a, b) in R, (b, a) must be in R
    is_symmetric = all((b, a) in R for (a, b) in R)
    
    # Check if R is antisymmetric: For all (a, b) in R, if a != b then (b, a) not in R
    # Not needed for equivalence, but included for completeness
    is_antisymmetric = all((a != b) or ((b, a) not in R) for (a, b) in R)
    
    # Check if R is transitive: For all (a, b) and (b, c) in R, (a, c) must be in R
    is_transitive = True
    for (a, b) in R:
        for (b2, c) in R:
            if b == b2:
                if (a, c) not in R:
                    is_transitive = False
                    break
        if not is_transitive:
            break
    
    return is_reflexive, is_symmetric, is_transitive

# Set A and relation R (candidate for equivalence relation)
A = {1, 2, 3, 4}
R = {(1, 1), (2, 2), (3, 3), (4, 4), (1, 3), (3, 1)}

# Check properties
reflexive, symmetric, transitive = check_relation_properties(A, R)

# Verify if R is an equivalence relation
if reflexive and symmetric and transitive:
    print("R is an equivalence relation.")
else:
    print("R is NOT an equivalence relation.")

# Test with another relation that does NOT satisfy one property
R2 = {(1, 1), (2, 2), (3, 3), (4, 4), (1, 3)}  # Missing (3, 1), so not symmetric
reflexive2, symmetric2, transitive2 = check_relation_properties(A, R2)

print("\nTest relation R2:")
if reflexive2 and symmetric2 and transitive2:
    print("R2 is an equivalence relation.")
else:
    print("R2 is NOT an equivalence relation.")