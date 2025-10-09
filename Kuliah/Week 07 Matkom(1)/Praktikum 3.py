# kursus_a = {"Deny", "Budi", "Citra", "Dewi"}
# kursus_b = {"Fahri", "Gina", "Hadi", "Ira"}

# # Cek apakah kedua himpunan ekivalen
# def cek_himpunan_ekivalen(set_a, set_b):
#     return len(set_a) == len(set_b)

# if cek_himpunan_ekivalen(kursus_a, kursus_b):
#     print("Kedua himpunan ekivalen.")
# else:
#     print("Kedua himpunan tidak ekivalen.")

# matkom = {"Deny", "Budi", "Citra", "Dewi"}
# strukdat = {"Eko", "Farhan", "Gita", "Hadi"}

# # Cek apakah kedua himpunan saling lepas
# def cek_himpunan_lepas(set_a, set_b):
#     return set_a.isdisjoint(set_b)

# if cek_himpunan_lepas(matkom, strukdat):
#     print("Kedua himpunan saling lepas.")
# else:
#     print("Kedua himpunan memiliki elemen yang sama.")

# from itertools import chain, combinations

# def himpunan_kuasa(s):
#     return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

# kursus = {"Deny", "Budi", "Citra"}
# kuasa = himpunan_kuasa(kursus)
# print("Himpunan Kuasa:", kuasa)

matkom = {"Deny", "Budi", "Citra", "Dewi"}
strukdat = {"Citra", "Dewi", "Eko", "Farhan"}

# Operasi gabungan (union)
gabungan = matkom.union(strukdat)
print("Gabungan:", gabungan)

# Operasi irisan (intersection)
irisan = matkom.intersection(strukdat)
print("Irisan:", irisan)

# Operasi selisih (difference)
selisih = matkom.difference(strukdat)
print("Selisih (Matkom - Strukdat):", selisih)
