# Number 1
import numpy as np

def matrix_operations(A, B):
    """
    Function to perform addition, subtraction, and multiplication 
    on two given matrices using NumPy.
    """
    
    # --- 1. Addition (A + B) ---
    # NumPy allows element-wise addition directly with the + operator
    addition_result = A + B
    print("1. Addition (A + B):\n", addition_result)
    
    # --- 2. Subtraction (2A - B) ---
    # First multiply matrix A by scalar 2, then subtract matrix B
    subtraction_result = (2 * A) - B
    print("\n2. Subtraction (2A - B):\n", subtraction_result)
    
    # --- 3. Multiplication (A x B) ---
    # Use the @ operator or np.dot() for matrix multiplication
    mul_AB = A @ B
    print("\n3. Multiplication (A x B):\n", mul_AB)
    
    # --- 4. Multiplication (B x A) ---
    mul_BA = B @ A
    print("\n4. Multiplication (B x A):\n", mul_BA)
    
    # --- 5. Check Commutativity (A x B = B x A) ---
    # np.array_equal checks if both arrays contain the exact same elements
    is_equal = np.array_equal(mul_AB, mul_BA)
    
    print("\n--- Commutativity Check ---")
    if is_equal:
        print("Result: A x B is equal to B x A (Commutative).")
    else:
        print("Result: A x B is NOT equal to B x A (Not Commutative).")

# --- Main Execution ---

# Define Matrix A and B using NumPy arrays
A = np.array([[1, 2], 
              [3, 4]])

B = np.array([[2, 0], 
              [1, 3]])

# Call the function
matrix_operations(A, B)

# Number 2
def generate_relation(A, B):
    """
    Generate all ordered pairs (a, b) from sets A and B 
    that satisfy a given rule.
    """
    
    # --- Relation 1: b = 2a ---
    relation_double = []  # list to store pairs satisfying b = 2a
    for a in A:
        for b in B:
            if b == 2 * a:      # check relation rule
                relation_double.append((a, b))
    
    print("Relation R (b = 2a):", relation_double)
    
    # --- Relation 2: b = a^2 ---
    relation_square = []  # list to store pairs satisfying b = a^2
    for a in A:
        for b in B:
            if b == a**2:      # check square relation rule
                relation_square.append((a, b))
                
    print("Relation for b = a^2:", relation_square)


# --- Test Data ---
A = {1, 2, 3, 4}
B = {2, 4, 6, 8}

# --- Run the function ---
generate_relation(A, B)

# Number 3
def relation_table(A, B, R):
    """
    Display the relation R in table form.
    Uses V if (a, b) is in R and – if not.
    """
    
    # Convert sets to sorted lists for consistent table order
    A = sorted(A)
    B = sorted(B)
    
    # Print header row
    print("    ", end="")
    for b in B:
        print(f"{b:>3}", end="")
    print()
    
    # Print each row for elements of A
    for a in A:
        print(f"{a:>3} ", end="")
        for b in B:
            # Check whether the pair (a, b) is in relation R
            if (a, b) in R:
                print(" V ", end="")
            else:
                print(" – ", end="")
        print()


# --- Given Data ---
A = {1, 2, 3, 4}
B = {2, 4, 6, 8}
R = {(1,2), (2,4), (3,6), (4,8)}

# Run the function
relation_table(A, B, R)

# Number 4
def relation_matrix(A, B, R):
    """
    Create and display the binary matrix for relation R
    using 1 if (a, b) is in R and 0 otherwise.
    """
    
    # Sort sets for consistent matrix order
    A = sorted(A)
    B = sorted(B)

    # Initialize an empty 2‑dimensional list (matrix)
    matrix = []

    # Loop over every element a in A (rows)
    for a in A:
        row = []
        # Loop over every element b in B (columns)
        for b in B:
            # Append 1 if (a, b) is in the relation, else 0
            row.append(1 if (a, b) in R else 0)
        matrix.append(row)

    # Display the resulting matrix
    print("Relation Matrix (A × B):")
    for row in matrix:
        print(row)

    return matrix


# Given data
A = {1, 2, 3, 4}
B = {2, 4, 6, 8}
R = {(1,2), (2,4), (3,6), (4,8)}

# Run the function
relation_matrix(A, B, R)

# Number 5
import networkx as nx
import matplotlib.pyplot as plt

def draw_relation_graph(A, B, R):
    """
    Draw a directed graph for relation R using networkx and matplotlib.
    Nodes come from sets A and B, and edges follow the ordered pairs in R.
    """

    # Create a directed graph object
    G = nx.DiGraph()

    # Add nodes from A and B
    G.add_nodes_from(A)
    G.add_nodes_from(B)

    # Add directed edges based on relation R
    for (a, b) in R:
        G.add_edge(a, b)

    # Create a layout for positioning nodes visually
    pos = nx.spring_layout(G)

    # Draw the nodes, edges, and labels
    nx.draw(G, pos, with_labels=True, arrows=True, node_color="lightblue", node_size=800)

    # Add a title
    plt.title("Directed Graph of Relation R")

    # Show the graph
    plt.show()


# Given data
A = {1, 2, 3, 4}
B = {2, 4, 6, 8}
R = {(1,2), (2,4), (3,6), (4,8)}

# Run the function
draw_relation_graph(A, B, R)