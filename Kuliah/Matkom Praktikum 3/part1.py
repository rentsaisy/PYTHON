# Number 1
from tokenize import Number
import numpy as np

sales = np.array([
    [100, 150, 200],
    [80, 120, 160]
])

total_sales_per_region = np.sum(sales, axis=0)
print("Sales matrix:")
print(sales)
print("Total sales per region:", total_sales_per_region)

# Number 2
A = {1, 2, 3}

relation = [(a, b) for a in A for b in A if a < b]
print("Pairs in the 'less than' relation:", relation)

# Number 3
B = [1, 2, 4]
relation_table = []

for i in B:
    row = []
    for j in B:
        if i % j == 0:
            row.append(1)
        else:
            row.append(0)
    relation_table.append(row)

print("Relation table for 'multiple of':")
for row in relation_table:
    print(row)

# Number 4
C = [1, 2, 3]
relation_matrix = []

for i in C:
    row = []
    for j in C:
        if i > j:
            row.append(1)
        else:
            row.append(0)
    relation_matrix.append(row)

print("Matrix for the 'greater than' relation:")
for row in relation_matrix:
    print(row)

# Number 5
import networkx as nx
import matplotlib.pyplot as plt

people = ["Deny", "Budi", "Cici"]
friend_relation = [("Deny", "Budi"), ("Budi", "Cici")]

G = nx.Graph()
G.add_nodes_from(people)
G.add_edges_from(friend_relation)

plt.figure(figsize=(5, 5))
nx.draw(
    G,
    with_labels=True,
    node_color='lightgreen',
    font_size=10,
    font_weight='bold',
    arrowsize=20
)
plt.title("Directed graph for the 'Friend' relation")
plt.show()