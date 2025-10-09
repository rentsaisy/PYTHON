# # # # Data himpunan mahasiswa dari tiga kelas
# # # matkom = {'Alya', 'Budi', 'Chandra', 'Diana'}
# # # strukdat = {'Budi', 'Diana', 'Eka', 'Farhan'}
# # # alpro = {'Alya', 'Farhan', 'Gilang'}

# # # # 1. Gabungkan seluruh mahasiswa dari ketiga kelas
# # # union_students = matkom.union(strukdat, alpro)

# # # # 2. Temukan mahasiswa yang mengikuti ketiga kelas
# # # intersection_students = matkom.intersection(strukdat, alpro)

# # # # 3. Temukan mahasiswa yang hanya mengikuti satu kelas (contoh: hanya di Alpro)
# # # only_alpro = alpro.difference(matkom.union(strukdat))

# # # # Output hasil
# # # print(f"Gabungan mahasiswa dari ketiga kelas: {union_students}")
# # # print(f"Irisan mahasiswa dari ketiga kelas: {intersection_students}")
# # # print(f"Mahasiswa yang hanya mengikuti kelas Alpro: {only_alpro}")

# # # Data pelanggan dari tiga toko
# # toko_a = {'Alya', 'Budi', 'Chandra'}
# # toko_b = {'Budi', 'Diana', 'Eka'}
# # toko_c = {'Alya', 'Farhan', 'Gilang'}

# # # 1. Hukum Komutatif: (A ∪ B) = (B ∪ A)
# # commutative_union = toko_a.union(toko_b) == toko_b.union(toko_a)

# # # 2. Hukum Asosiatif: A ∪ (B ∪ C) = (A ∪ B) ∪ C
# # associative_union = toko_a.union(toko_b.union(toko_c)) == toko_a.union(toko_b).union(toko_c)

# # # Output hasil
# # print(f"Hukum Komutatif berlaku: {commutative_union}")
# # print(f"Hukum Asosiatif berlaku: {associative_union}")

# # Data produk per toko
# toko_a = {'Laptop', 'Mouse', 'Keyboard'}
# toko_b = {'Mouse', 'Printer', 'Monitor'}
# toko_c = {'Laptop', 'Printer', 'Mouse'}

# # Semesta produk (U) = semua produk yang muncul di mana pun
# U = toko_a | toko_b | toko_c

# # 1) Produk yang dijual oleh setidaknya satu toko  (union)
# produk_union = toko_a | toko_b | toko_c

# # 2) Produk yang dijual oleh semua toko (intersection)
# produk_intersection = toko_a & toko_b & toko_c

# # — Duality checks (De Morgan) —
# # A ∪ B ∪ C = U \ ((U\A) ∩ (U\B) ∩ (U\C))
# dual_union = U - ((U - toko_a) & (U - toko_b) & (U - toko_c))

# # A ∩ B ∩ C = U \ ((U\A) ∪ (U\B) ∪ (U\C))
# dual_intersection = U - ((U - toko_a) | (U - toko_b) | (U - toko_c))

# print("Produk (gabungan semua toko):", produk_union)
# print("Produk (dijual oleh semua toko):", produk_intersection)
# print("Dual check — union equals dual_union? ->", produk_union == dual_union)
# print("Dual check — intersection equals dual_intersection? ->", produk_intersection == dual_intersection)

# Data pelanggan dari tiga cabang bank
cabang_a = {'Alya', 'Budi', 'Chandra'}
cabang_b = {'Budi', 'Diana', 'Eka'}
cabang_c = {'Alya', 'Farhan', 'Gilang'}

# Menghitung total pelanggan unik dengan prinsip inklusi–eksklusi
total_unik = (
    len(cabang_a)
    + len(cabang_b)
    + len(cabang_c)
    - len(cabang_a & cabang_b)
    - len(cabang_a & cabang_c)
    - len(cabang_b & cabang_c)
    + len(cabang_a & cabang_b & cabang_c)
)

print(f"Jumlah total pelanggan unik dari tiga cabang: {total_unik}")
