matkom = {"Deny", "Budi", "Citra", "Dewi", "Eko"}
strukdat = {"Budi", "Citra", "Eko", "Farhan", "Gita"}

mahasiswa_kedua_kelas = matkom.intersection(strukdat)
print(f"Mahasiswa yang mengambil kedua kelas: {mahasiswa_kedua_kelas}")

mahasiswa_satu_kelas = matkom.symmetric_difference(strukdat)
print(f"Mahasiswa yang hanya mengambil satu kelas: {mahasiswa_satu_kelas}")

total_mahasiswa = matkom.union(strukdat)
print(f"Total mahasiswa yang hadir di setidaknya salah satu kelas: {len(total_mahasiswa)}")

matkom_subset_strukdat = matkom.issubset(strukdat)
if matkom_subset_strukdat:
    print("Semua mahasiswa yang hadir di Matematika Komputasi juga hadir di Struktur Data.")
else:
    print("Tidak semua mahasiswa yang hadir di Matematika Komputasi hadir di Struktur Data.")

if len(matkom) == len(strukdat):
    print("Jumlah mahasiswa yang hadir di kedua kelas sama.")
else:
    print("Jumlah mahasiswa yang hadir di kedua kelas berbeda.")