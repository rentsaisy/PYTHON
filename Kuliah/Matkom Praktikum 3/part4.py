# Number 1
relation_R = [(1, 2), (2, 3), (3, 4)]

inverse_relation = [(b, a) for (a, b) in relation_R]

print("Relation R :", relation_R)
print("Inverse relation R^-1 :", inverse_relation)
print("=" * 40)

# Number 2
relation_R = [(1, 2), (2, 3)]

relation_S = [(2, 4), (3, 5)]

combined_relation = relation_R + relation_S

print("Relation R:", relation_R)
print("Relation S:", relation_S)
print("Combined Relation:", combined_relation)
print("=" * 40)

# Number 3
relation_R = [(1, 2), (2, 3)]

relation_S = [(2, 3), (3, 4)]

composition_relation = [(a, d) for (a, b) in relation_R for (c, d) in relation_S if b == c]

print("Relation R:", relation_R)
print("Relation S:", relation_S)
print("Composition R ○ S:", composition_relation)
print("=" * 40)

# Number 4
relation_R = [(1, 1), (2, 2), (1, 2), (2, 1)]

set_A = {1, 2}

is_reflexive = all((a, a) in relation_R for a in set_A)

is_symmetric = all((b, a) in relation_R for (a, b) in relation_R)

is_transitive = all(
    (a, c) in relation_R
    for (a, b) in relation_R
    for (c, d) in relation_R
    if b == c
)

print("Relation R:", relation_R)
print("Reflexive:", is_reflexive)
print("Symmetric:", is_symmetric)
print("Transitive:", is_transitive)
print("=" * 40)

# Number 5
relation_R = [(1, 1), (2, 2), (1, 2), (2, 1)]

set_A = {1, 2}

is_reflexive = all((a, a) in relation_R for a in set_A)

is_symmetric = all((b, a) in relation_R for (a, b) in relation_R)

is_transitive = all(
    (a, c) in relation_R
    for (a, b) in relation_R
    for (c, d) in relation_R
    if b == c
)

is_equivalence = is_reflexive and is_symmetric and is_transitive

print("Relation R:", relation_R)
print("Is R an equivalence relation?:", is_equivalence)
print("=" * 40)
