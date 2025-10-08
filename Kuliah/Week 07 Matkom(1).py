set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(len(set_a)==len(set_b))
print("Size set A:", len(set_a))

set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.isdisjoint(set_b))

from itertools import chain, combinations

def power_set(s):
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

set_a = {1, 2, 3}
print(power_set(set_a))

# Himpunan A dan B
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Himpunan semesta adalah gabungan dari set_a dan set_b
himpunan_semesta = set_a.union(set_b)

# Operasi Gabungan (Union)
union = set_a.union(set_b)

# Operasi Irisan (Intersection)
intersection = set_a.intersection(set_b)

# Operasi Selisih (Difference)
difference_a_b = set_a.difference(set_b)

# Operasi Komplemen (Complement)
complement_a = himpunan_semesta.difference(set_a)
complement_b = himpunan_semesta.difference(set_b)

# Menampilkan hasil operasi
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Gabungan (A ∪ B): {union}")
print(f"Irisan (A ∩ B): {intersection}")
print(f"Selisih (A - B): {difference_a_b}")
print(f"Komplemen (Semesta - A): {complement_a}")
print(f"Komplemen (Semesta - B): {complement_b}")
