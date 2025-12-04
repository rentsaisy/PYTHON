# Number 1
# Function to check whether a relation R on set A is a partial order
def is_partial_order(A, R):
    # Convert to sets for easy membership tests
    A = set(A)
    R = set(R)

    # Check reflexivity: every (a, a) must be in R
    reflexive = all((a, a) in R for a in A)

    # Check antisymmetry: if (a, b) and (b, a) in R, then a == b
    antisymmetric = True
    for a, b in R:
        if (b, a) in R and a != b:
            antisymmetric = False
            break

    # Check transitivity: if (a, b) and (b, c) in R, then (a, c) must be in R
    transitive = True
    for a, b in R:
        for x, c in R:
            if b == x and (a, c) not in R:
                transitive = False
                break
        if not transitive:
            break

    # Display results
    print("Reflexive:", reflexive)
    print("Antisymmetric:", antisymmetric)
    print("Transitive:", transitive)
    print("Is partial order:", reflexive and antisymmetric and transitive)

    return reflexive and antisymmetric and transitive

# Example use
A = {1, 2, 3, 4}
R = {(1,1),(2,2),(3,3),(4,4),(1,2),(2,3),(1,3)}

is_partial_order(A, R)

# Number 2
# Build the reflexive closure of R on set A
def reflexive_closure(A, R):
    R = set(R)
    for a in A:
        # Add missing (a,a) pairs
        if (a, a) not in R:
            R.add((a, a))
    return R

# Build the symmetric closure of R
def symmetric_closure(R):
    R = set(R)
    for a, b in list(R):
        # Add (b,a) if missing
        if (b, a) not in R:
            R.add((b, a))
    return R

# Build the transitive closure of R
def transitive_closure(R):
    R = set(R)
    added = True

    # Keep adding (a,c) whenever (a,b) and (b,c) are present
    while added:
        added = False
        new_pairs = set()
        for a, b in R:
            for x, c in R:
                if b == x and (a, c) not in R:
                    new_pairs.add((a, c))
        if new_pairs:
            R |= new_pairs
            added = True
    return R

# Example usage
A = {1, 2, 3}
R = {(1,2), (2,3)}

print("Reflexive closure:", reflexive_closure(A, R))
print("Symmetric closure:", symmetric_closure(R))
print("Transitive closure:", transitive_closure(R))

# Number 3
# Function to display a 3‑ary relation in a simple table
def display_nary_relation(R):
    # Print header
    print("Mahasiswa\tMata Kuliah\tNilai")
    print("-----------------------------------------")
    
    # Loop through each tuple and print in formatted columns
    for student, course, grade in R:
        print(f"{student}\t{course}\t{grade}")

# Original relation
R = {
    ("Andi", "Matematika", 90),
    ("Budi", "Fisika", 85),
    ("Citra", "Kimia", 88)
}

# Add a few new data points for testing
R.add(("Dina", "Biologi", 92))
R.add(("Eko", "Matematika", 78))

# Display the full relation
display_nary_relation(R)

# Number 4 
# Check whether a relation R from A to B is a function
def is_function(A, B, R):
    A = set(A)
    B = set(B)
    R = set(R)

    # Track mappings from elements of A
    mapping = {}

    for a, b in R:
        # Reject if a is not in A or b is not in B
        if a not in A or b not in B:
            return False

        # Reject if a maps to more than one value
        if a in mapping and mapping[a] != b:
            return False

        mapping[a] = b

    # Every element of A must have exactly one output
    if len(mapping) != len(A):
        return False

    return True


# Given sets and relation
A = {1, 2, 3, 4}
B = {2, 4, 6, 8}
R = {(1,2),(2,4),(3,6),(4,8)}

# Display result
print("Relation R:", R)
print("Is R a function from A to B?", is_function(A, B, R)) 