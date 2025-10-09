# # # set_a = {1, 2, 3}
# # # set_b = {2, 3, 4}
# # # set_c = {3, 4, 5}

# # # # Operasi gabungan
# # # union_set = set_a.union(set_b, set_c)

# # # # Operasi irisan
# # # intersection_set = set_a.intersection(set_b, set_c)

# # # # Operasi selisih
# # # difference_set = set_a.difference(set_b.union(set_c))

# # # print(f"Gabungan: {union_set}")
# # # print(f"Irisan: {intersection_set}")
# # # print(f"Selisih: {difference_set}")

# # set_a = {1, 2}
# # set_b = {2, 3}
# # set_c = {3, 4}

# # # Hukum Komutatif (A ∪ B = B ∪ A)
# # commutative_union = set_a.union(set_b) == set_b.union(set_a)
# # commutative_intersection = set_a.intersection(set_b) == set_b.intersection(set_a)

# # # Hukum Asosiatif (A ∪ (B ∪ C) = (A ∪ B) ∪ C)
# # associative_union = set_a.union(set_b.union(set_c)) == set_a.union(set_b).union(set_c)
# # associative_intersection = set_a.intersection(set_b.intersection(set_c)) == set_a.intersection(set_b).intersection(set_c)

# # # Hukum Distributif (A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C))
# # distributive_union_intersection = set_a.union(set_b.intersection(set_c)) == (set_a.union(set_b)).intersection(set_a.union(set_c))

# # print(f"Hukum Komutatif: {commutative_union and commutative_intersection}")
# # print(f"Hukum Asosiatif: {associative_union and associative_intersection}")
# # print(f"Hukum Distributif: {distributive_union_intersection}")

# set_a = {1, 2}
# set_b = {2, 3}
# set_c = {3, 4}

# # Pernyataan asli (A ∪ (B ∩ C))
# original_statement = set_a.union(set_b.intersection(set_c))

# # Pernyataan dual (A ∩ (B ∪ C))
# dual_statement = set_a.intersection(set_b.union(set_c))

# print(f"Pernyataan Asli: {original_statement}")
# print(f"Pernyataan Dual: {dual_statement}")

set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_c = {5, 6, 7}

# Menghitung ukuran gabungan menggunakan prinsip inklusi-eksklusi
total_union = len(set_a) + len(set_b) + len(set_c) \
    - len(set_a.intersection(set_b)) \
    - len(set_a.intersection(set_c)) \
    - len(set_b.intersection(set_c)) \
    + len(set_a.intersection(set_b).intersection(set_c))

print(f"Ukuran gabungan tiga himpunan (A ∪ B ∪ C): {total_union}")
