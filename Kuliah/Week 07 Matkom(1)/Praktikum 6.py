# # # python_class = {'Alya', 'Deny', 'Chandra', 'Diana'}
# # # java_class = {'Deny', 'Diana', 'Eka', 'Farhan'}
# # # cpp_class = {'Alya', 'Farhan', 'Gilang'}

# # # union_students = python_class.union(java_class, cpp_class)
# # # intersection_students = python_class.intersection(java_class, cpp_class)
# # # difference_students = python_class.difference(java_class.union(cpp_class))

# # # print(f"Gabungan Siswa: {union_students}")
# # # print(f"Siswa yang mengikuti ketiga kelas: {intersection_students}")
# # # print(f"Siswa yang hanya mengikuti Kelas Python: {difference_students}")

# # store_a = {'Alya', 'Deny', 'Chandra'}
# # store_b = {'Deny', 'Diana', 'Eka'}
# # store_c = {'Alya', 'Farhan', 'Gilang'}

# # # Hukum Komutatif (A ∪ B = B ∪ A)
# # commutative_union = store_a.union(store_b) == store_b.union(store_a)

# # # Hukum Asosiatif (A ∪ (B ∪ C) = (A ∪ B) ∪ C)
# # associative_union = store_a.union(store_b.union(store_c)) == store_a.union(store_b).union(store_c)

# # print(f"Hukum Komutatif berlaku: {commutative_union}")
# # print(f"Hukum Asosiatif berlaku: {associative_union}")

# store_a = {'Laptop', 'Mouse', 'Keyboard'}
# store_b = {'Mouse', 'Printer', 'Monitor'}
# store_c = {'Laptop', 'Printer', 'Mouse'}

# union_products = store_a.union(store_b, store_c)
# intersection_products = store_a.intersection(store_b, store_c)

# print(f"Produk yang dijual oleh setidaknya satu toko: {union_products}")
# print(f"Produk yang dijual oleh semua toko: {intersection_products}")

branch_a = {'Alya', 'Budi', 'Chandra'}
branch_b = {'Budi', 'Diana', 'Eka'}
branch_c = {'Alya', 'Farhan', 'Gilang'}

total_unique_customers = len(branch_a) + len(branch_b) + len(branch_c) \
    - len(branch_a.intersection(branch_b)) - len(branch_a.intersection(branch_c)) \
    - len(branch_b.intersection(branch_c)) + len(branch_a.intersection(branch_b).intersection(branch_c))

print(f"Jumlah pelanggan unik: {total_unique_customers}")
