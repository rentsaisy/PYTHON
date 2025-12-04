matkom   = {"Deny", "Budi", "Citra", "Dewi", "Eko"}
strukdat = {"Budi", "Citra", "Eko", "Farhan", "Gita"}

# ---------- Helper ----------
def show_section(title: str):
    print("\n" + "="*len(title))
    print(title)
    print("="*len(title))

# ---------- Langkah 1: Analisis dua kelas (Matkom vs Strukdat) ----------
show_section("Langkah 1: Matematika Komputasi vs Struktur Data")

kedua = matkom.intersection(strukdat)
satu_saja = matkom.symmetric_difference(strukdat)
total = matkom.union(strukdat)

print(f"Mahasiswa yang hadir di kedua kelas: {sorted(kedua)}")
print(f"Mahasiswa yang hanya hadir di salah satu kelas: {sorted(satu_saja)}")
print(f"Total mahasiswa unik (setidaknya salah satu kelas): {len(total)}  -> {sorted(total)}")

# ---------- Langkah 2: Modifikasi – dua mata kuliah tambahan ----------

# Langkah 2 (dua kelas tambahan, gunakan daftar nama berbeda)
algoritma = {"Ani", "Budi", "Cici", "Dodi", "Eka"}
basisdata = {"Bima", "Cici", "Dodi", "Fina", "Gilang"}

show_section("Langkah 2: Algoritma vs Basis Data (analisis serupa)")

kedua_AB = algoritma.intersection(basisdata)
satu_saja_AB = algoritma.symmetric_difference(basisdata)
total_AB = algoritma.union(basisdata)

print(f"Mahasiswa yang hadir di kedua kelas (Algoritma & Basis Data): {sorted(kedua_AB)}")
print(f"Mahasiswa yang hanya hadir di salah satu (Algoritma xor Basis Data): {sorted(satu_saja_AB)}")
print(f"Total mahasiswa unik (Algoritma U Basis Data): {len(total_AB)}  -> {sorted(total_AB)}")

# ---------- Langkah 3: Analisis tiga kelas ----------
show_section("Langkah 3: Analisis tiga kelas (Struktur Data & Algoritma)")

irisan_SD_ALGO = strukdat.intersection(algoritma)
print(f"Poin 1 - Hadir di Strukdat dan Algoritma: {sorted(irisan_SD_ALGO)}")

symdiff_SD_ALGO = strukdat.symmetric_difference(algoritma)
print(f"Poin 2 - Hanya di salah satu (Strukdat atau Algoritma): {sorted(symdiff_SD_ALGO)}")

union_SD_ALGO = strukdat.union(algoritma)
print(f"Poin 3 - Total unik (Strukdat U Algoritma): {len(union_SD_ALGO)}  -> {sorted(union_SD_ALGO)}")

show_section("Poin 4 - Subset Check (Matkom dengan Strukdat)")
if matkom.issubset(strukdat):
    print("Semua mahasiswa Matematika Komputasi juga hadir di Struktur Data. (True)")
else:
    print("Tidak semua mahasiswa Matematika Komputasi hadir di Struktur Data. (False)")

show_section("Poin 5 - Equal Sets (Cardinality)")
print(f"|Matkom| = {len(matkom)}, |Strukdat| = {len(strukdat)}")
if len(matkom) == len(strukdat):
    print("Jumlah mahasiswa kedua kelas SAMA.")
else:
    print("Jumlah mahasiswa kedua kelas BERBEDA.")

# ---------- Bonus: Empty set ----------
show_section("Empty Set (opsional di laporan)")
himpunan_kosong = set()
print(f"Himpunan kosong direpresentasikan sebagai: {himpunan_kosong}")
