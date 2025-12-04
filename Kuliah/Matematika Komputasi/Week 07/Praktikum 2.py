def equivalent_sets():
    print("=== Himpunan yang ekuivalen ===")
    set_a = {1, 2, 3, 4}
    set_b = {5, 6, 7, 8}
    
    # Cek  apakah kedua himpunan ekuivalen (memiliki ukuran yang sama)
    are_equivalent = len(set_a) == len(set_b)
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Apakah kedua himpunan ekuivalen? {are_equivalent}")
    print("===============================\n")
    
def disjoint_sets():
    print("=== Himpunan yang saling lepas ===")
    set_a = {1, 2, 3}
    set_b = {4, 5, 6}
    
    # Cek apakah kedua himpunan saling lepas (tidak memiliki elemen yang sama)
    are_disjoint = set_a.isdisjoint(set_b)
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Apakah kedua himpunan saling lepas? {are_disjoint}")
    print("==================================\n")
    
def power_set(s):
    print("=== Himpunan Kuasa ===")
    from itertools import chain, combinations
    
    def power_set_generator(s):
        return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    
    # Himpunan kuasa dari himpunan s
    p_set = power_set_generator(s)
    print(f"Himpunan: {s}")
    print(f"Himpunan Kuasa: {p_set}")
    print("===============================\n")
    
def set_operations():
    print("=== Operasi Himpunan ===")
    # Himpunan A dan B
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    
    # Himpunan semesta adalah gabungan dari set_a dan set_b
    himpunan_semesta = set_a.union(set_b)
    
    # Operasi Gabungan (Union)
    union_set = set_a.union(set_b)
    
    # Operasi Irisan (Intersection)
    intersection_set = set_a.intersection(set_b)
    
    # Operasi Selisih (Difference)
    difference_set = set_a.difference(set_b)
    
    # Operasi Komplemen (Complement)
    complement_a = himpunan_semesta.difference(set_a)
    complement_b = himpunan_semesta.difference(set_b)
    
    # Menampilkan hasil operasi
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Gabungan (A ∪ B): {union_set}")
    print(f"Irisan (A ∩ B): {intersection_set}")    
    print(f"Selisih (A - B): {difference_set}")
    print(f"Komplemen A (Semesta - A): {complement_a}")
    print(f"Komplemen B (Semesta - B): {complement_b}")
    print("===============================\n")
    
if __name__ == "__main__":
    equivalent_sets()
    disjoint_sets()
    power_set({1, 2, 3})
    set_operations()
