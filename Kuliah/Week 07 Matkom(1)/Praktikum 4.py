# # Membandingkan Himpunan Ekivalen dan Saling Lepas

# KelasA = {"Aisyah", "Rifdah", "Amel"}
# KelasB = {"Soraya", "Elvira", "Ares", "Afi"}

# # Mengecek ekivalen
# if len(KelasA) == len(KelasB):
#     print("Kedua himpunan ekivalen (jumlah elemennya sama).")
# else:
#     print("Kedua himpunan tidak ekivalen (jumlah elemennya berbeda).")

# # Mengecek saling lepas
# if KelasA.isdisjoint(KelasB):
#     print("Kedua himpunan saling lepas (tidak ada anggota yang sama).")
# else:
#     print("Kedua himpunan tidak saling lepas (ada anggota yang sama).")

# Program Memeriksa Himpunan Saling Lepas

# AcaraA = {"Aisyah", "Rifdah", "Amel"}
# AcaraB = {"Soraya", "Elvira", "Ares", "Afi"}

# # Mengecek apakah kedua himpunan saling lepas
# if AcaraA.isdisjoint(AcaraB):
#     print("Kedua himpunan saling lepas (tidak ada anggota yang sama).")
# else:
#     print("Kedua himpunan tidak saling lepas (ada anggota yang sama).")

# # Program Menghasilkan Himpunan Kuasa
# import itertools

# # Himpunan mahasiswa Kelas A
# MahasiswaKelasA = {"Aisyah", "Rifdah", "Amel", "Soraya", "Elvira", "Ares", "Afi"}

# print("Mahasiswa Kelas A:", MahasiswaKelasA)
# print("-" * 50)

# # Membuat list kosong untuk menampung semua subset (himpunan kuasa)
# himpunan_kuasa = []

# # Menghasilkan semua kombinasi elemen dari ukuran 0 hingga n
# for i in range(len(MahasiswaKelasA) + 1):
#     kombinasi = itertools.combinations(MahasiswaKelasA, i)
#     for subset in kombinasi:
#         himpunan_kuasa.append(set(subset))

# # Menampilkan semua himpunan kuasa
# print("Himpunan Kuasa dari Mahasiswa Kelas A adalah:")
# for h in himpunan_kuasa:
#     print(h)

# # Menampilkan jumlah total subset
# print("-" * 50)
# print(f"Total himpunan kuasa: {len(himpunan_kuasa)}")

# # Program Operasi Terhadap Himpunan

# # Membuat dua himpunan mahasiswa dari dua mata kuliah berbeda
# MatematikaKomputasi = {"Aisyah", "Rifdah", "Amel"}
# StrukturData = {"Soraya", "Elvira", "Ares", "Afi", "Amel", "Rifdah"}

# # Menampilkan data awal
# print("Mahasiswa Matematika Komputasi:", MatematikaKomputasi)
# print("Mahasiswa Struktur Data:", StrukturData)

# # 1. Gabungan (Union)
# gabungan = MatematikaKomputasi.union(StrukturData)
# print("1. Gabungan (Union):", gabungan)

# # 2. Irisan (Intersection)
# irisan = MatematikaKomputasi.intersection(StrukturData)
# print("2. Irisan (Intersection):", irisan)

# # 3. Selisih (Difference)
# selisih = MatematikaKomputasi.difference(StrukturData)
# print("3. Selisih (Difference):", selisih)

# # 4. Komplemen (Complement)
# # Misalkan himpunan semesta berisi semua mahasiswa dari kedua kelas
# semesta = {"Aisyah", "Rifdah", "Amel", "Soraya", "Elvira", "Ares", "Afi", "Viandra"}
# komplemen = semesta.difference(gabungan)
# print("4. Komplemen (Complement):", komplemen)

