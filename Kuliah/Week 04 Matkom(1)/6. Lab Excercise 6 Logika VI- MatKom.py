def biconditional_logic_all_cases():
    print("=== Tabel Kebenaran Bikondisional dalam Jaringan Komputer ===")
    kasus = [(True, True), (True, False), (False, True), (False, False)]
    
    for p, q in kasus:
        bikondisional = (p and q) or (not p and not q)
        if bikondisional:
            hasil = "Perangkat berfungsi dengan baik."
        else:
            hasil = "Perangkat tidak sinkron."
        
        print(f"Perangkat A: {p}, Perangkat B: {q}, A <-> B: {bikondisional}, Hasil: {hasil}")
    print("=============================================================\n")

def inference_all_cases():
    print("=== Tabel Kebenaran Inferensi pada Sistem Alarm ===")
    kasus = [(True, True), (True, False), (False, True), (False, False)]

    for sensor_gerak, alarm_berbunyi in kasus:
        # p -> q setara dengan ¬p ∨ q
        implication = (not sensor_gerak) or alarm_berbunyi

        if implication:
            hasil = "Sistem berfungsi dengan baik."
        else:
            hasil = "Sistem gagal."

        print(f"Sensor: {sensor_gerak}, Alarm: {alarm_berbunyi}, p -> q: {implication}, Hasil: {hasil}")
    print("====================================================\n")

def argument_all_cases():
    print("=== Studi Kasus Argumen dalam Proses Bisnis ===")
    kasus = [
        (True, True, True),
        (True, True, False),
        (True, False, True),
        (True, False, False),
        (False, True, True),
        (False, True, False),
        (False, False, True),
        (False, False, False)
    ]

    for p, q, r in kasus:
        # Premis 1: p -> q
        premise_1 = (not p) or q
        # Premis 2: q -> r
        premise_2 = (not q) or r
        # Kesimpulan: p -> r
        conclusion = (not p) or r

        # Validasi: jika premis-premis benar, cek apakah kesimpulan juga benar
        if premise_1 and premise_2 and conclusion:
            hasil = "Kesimpulan benar: Perusahaan menerima bonus."
        elif premise_1 and premise_2 and not conclusion:
            hasil = "Kesimpulan salah: Tidak ada bonus."
        else:
            hasil = "Premis tidak terpenuhi, argumen tidak valid."

        print(f"Proyek: {p}, Klien puas: {q}, Bonus: {r} -> {hasil}")
    print("=============================================================\n")

def axioms_theorems_all_cases():
    print("=== Studi Kasus Aksioma, Teorema, Lemma, dan Corollary ===")
    # Beberapa kombinasi contoh segitiga
    kasus = [
        (90, 60, 30),   # Segitiga siku-siku
        (60, 60, 60),   # Segitiga sama sisi
        (100, 40, 40),  # Segitiga sembarang
        (120, 30, 30),  # Segitiga tumpul
        (100, 50, 20)   # Tidak valid (jumlah ≠ 180)
    ]

    for s1, s2, s3 in kasus:
        print(f"\nSudut 1: {s1}, Sudut 2: {s2}, Sudut 3: {s3}")

        # Aksioma: total sudut = 180
        if s1 + s2 + s3 != 180:
            print("Kesimpulan:  Bukan segitiga (melanggar Aksioma).")
            continue

        # Teorema & Corollary: ada sudut 90 → segitiga siku-siku
        if 90 in (s1, s2, s3):
            print("Kesimpulan (Teorema & Corollary): Ini adalah segitiga siku-siku.")
        else:
            print("Kesimpulan: Ini bukan segitiga siku-siku.")
    print("\n===========================================================\n")


# Jalankan semua kasus
axioms_theorems_all_cases()

# Jalankan semua kombinasi
argument_all_cases()

# Jalankan semua kasus
inference_all_cases()

# Menjalankan semua kasus
biconditional_logic_all_cases()
