# Number 1
import numpy as np

matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix A:\n", matrix_a)

matrix_b = np.array([[1, 1], [2, 2]])
matrix_c = np.array([[3, 3], [4, 4]])
result_add = matrix_b + matrix_c
print("\nMatrix Addition (B + C):\n", result_add)

transpose_a = np.transpose(matrix_a)
print("\nTranspose of Matrix A:\n", transpose_a)

# Number 2
A = {1, 2, 3}
B = {2, 4, 6}

relation = [(a, b) for a in A for b in B if b % a == 0]
print("Relation R:\n", relation)

def is_reflexive(relation, set_a):
    return all((a, a) in relation for a in set_a)

print("Is the relation reflexive?", is_reflexive(relation, A))

# Number 3
def create_relation_table(set_a, set_b, relation):
    table = [
        [1 if (a, b) in relation else 0 for b in set_b]
        for a in set_a
    ]
    return table

table = create_relation_table(A, B, relation)
for row in table:
    print(row)

# Number 4
def create_relation_matrix(set_a, set_b, relation):
    matrix = [
        [1 if (a, b) in relation else 0 for b in set_b]
        for a in set_a
    ]
    return np.array(matrix)

matrix = create_relation_matrix(A, B, relation)
print("Relation Matrix:\n", matrix)

# Number 5
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from(relation)

nx.draw(
    G,
    with_labels=True,
    node_size=700,
    node_color="skyblue",
    font_size=10,
    font_weight="bold"
)

plt.show()