# # # # Fungsi untuk memeriksa apakah partisi valid
# # # def is_valid_partition(original_set, partitions):
# # #     combined = set()  # untuk menyimpan semua elemen dari partisi
# # #     for part in partitions:
# # #         combined.update(part)  # gabungkan semua elemen partisi ke dalam satu set

# # #     # Valid jika: semua elemen himpunan muncul sekali dan tidak ada yang kosong
# # #     if combined == original_set and all(len(part) > 0 for part in partitions):
# # #         return True
# # #     return False


# # # # Himpunan asli (daftar karyawan)
# # # original_set = {'Adam', 'Bella', 'Charlie', 'Deny', 'Dewi', 'Eko', 'Farid'}

# # # # Dua partisi (tim)
# # # partitions = [
# # #     {'Adam', 'Bella', 'Charlie', 'Deny'},
# # #     {'Dewi', 'Eko', 'Farid'}
# # # ]

# # # # Cetak hasil pengecekan
# # # print(is_valid_partition(original_set, partitions))

# # # Fungsi untuk memverifikasi proposisi A ∩ (A ∪ B) = A
# # def verify_proposition(A, B):
# #     union_result = A.union(B)                    
# #     intersection_result = A.intersection(union_result)  
# #     return intersection_result == A                

# # # Himpunan contoh
# # A = {2, 4, 6}
# # B = {4, 6, 8}

# # # Cetak hasil verifikasi
# # print(verify_proposition(A, B))

# from collections import Counter

# # Fungsi untuk menghitung jumlah kemunculan setiap elemen
# def multiset_count(elements):
#     count = Counter(elements)
#     return count

# # Daftar multiset pesanan makanan
# food_orders = ['Nasi Goreng', 'Nasi Goreng', 'Sate', 'Sate', 'Sate', 'Soto']

# # Cetak hasil perhitungan
# print(multiset_count(food_orders))

# Fungsi untuk menghitung union (gabungan) dua himpunan fuzzy
def fuzzy_union(fuzzy_set_a, fuzzy_set_b):
    return {k: max(fuzzy_set_a.get(k, 0), fuzzy_set_b.get(k, 0)) for k in set(fuzzy_set_a) | set(fuzzy_set_b)}

# Fungsi untuk menghitung intersection (irisan) dua himpunan fuzzy
def fuzzy_intersection(fuzzy_set_a, fuzzy_set_b):
    return {k: min(fuzzy_set_a.get(k, 0), fuzzy_set_b.get(k, 0)) for k in set(fuzzy_set_a) & set(fuzzy_set_b)}

# Fungsi untuk menghitung complement (komplemen) dari himpunan fuzzy
def fuzzy_complement(fuzzy_set):
    return {k: 1 - v for k, v in fuzzy_set.items()}


# Himpunan fuzzy Matematika dan Fisika
fuzzy_math = {'Edo': 0.9, 'Rina': 0.7, 'Tari': 0.8}
fuzzy_physics = {'Edo': 0.6, 'Rina': 0.9, 'Tari': 0.5}

# Operasi fuzzy
union_result = fuzzy_union(fuzzy_math, fuzzy_physics)
intersection_result = fuzzy_intersection(fuzzy_math, fuzzy_physics)
complement_result = fuzzy_complement(fuzzy_math)

# Tampilkan hasil
print("Union Fuzzy:", union_result)
print("Intersection Fuzzy:", intersection_result)
print("Complement Fuzzy Matematika:", complement_result)
