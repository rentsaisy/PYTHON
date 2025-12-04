# Deklarasi himpunan dengan kurung kurawal
himpunan_a = {1, 2, 3, 4}

# Deklarasi himpunan dengan fungsi set()
himpunan_b = set([2, 3, 4, 5])

print(himpunan_a)
print(himpunan_b)
print("===============================================\n")

himpunan_a = {1, 2, 3, 4}
print("Kardinalitas himpunan A:", len(himpunan_a))
print("===============================================\n")

himpunan_kosong = set()
print("Himpunan kosong:" , himpunan_kosong)
print("===============================================\n")

himpunan_a = {1, 2, 3}
himpunan_b = {1, 2, 3, 4, 5}

print(himpunan_a.issubset(himpunan_b)) # Output: True
print("===============================================\n")

himpunan_a = {1, 2, 3}
himpunan_b = {3, 2, 1}

print(himpunan_a == himpunan_b) # Output: True
print("===============================================\n")
