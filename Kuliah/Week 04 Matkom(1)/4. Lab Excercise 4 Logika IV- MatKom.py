def biconditional_logic_case():
    print("=== Studi Kasus Bikondisional (Bi-implikasi) ===")
    perangkat_A = True   # Perangkat A berfungsi
    perangkat_B = False  # Perangkat B tidak berfungsi

    # A <-> B setara dengan (A ∧ B) ∨ (¬A ∧ ¬B)
    bikondisional = (perangkat_A and perangkat_B) or (not perangkat_A and not perangkat_B)

    print(f"Perangkat A: {perangkat_A}, Perangkat B: {perangkat_B}, A <-> B: {bikondisional}")
    print("===============================================\n")


def inference_case():
    print("=== Studi Kasus Inferensi ===")
    sensor_gerak = True     # Sensor mendeteksi gerakan
    alarm_berbunyi = False  # Alarm tidak berbunyi

    # p -> q setara dengan ¬p ∨ q
    implication = (not sensor_gerak) or alarm_berbunyi

    print(f"Sensor mendeteksi gerakan: {sensor_gerak}, Alarm berbunyi: {alarm_berbunyi}")
    print(f"p -> q: {implication}")
    if sensor_gerak and implication:
        print("Alarm harus berbunyi!")
    else:
        print("Sistem gagal mendeteksi pergerakan!")
    print("===============================================\n")


def argument_case():
    print("=== Studi Kasus Argumen ===")
    proyek_selesai_tepat_waktu = True   # Tim menyelesaikan proyek tepat waktu
    klien_puas = True                   # Klien puas
    perusahaan_terima_bonus = True       # Perusahaan menerima bonus

    # Premis 1: p -> q  == ¬p ∨ q
    premise_1 = (not proyek_selesai_tepat_waktu) or klien_puas
    # Premis 2: q -> r  == ¬q ∨ r
    premise_2 = (not klien_puas) or perusahaan_terima_bonus
    # Kesimpulan: p -> r == ¬p ∨ r
    conclusion = (not proyek_selesai_tepat_waktu) or perusahaan_terima_bonus

    print(f"Premis 1 (p -> q): {premise_1}")
    print(f"Premis 2 (q -> r): {premise_2}")
    print(f"Kesimpulan (p -> r): {conclusion}")
    print("===============================================\n")


def axioms_theorems_case():
    print("=== Studi Kasus Aksioma, Teorema, Lemma, dan Corollary ===")
    # Aksioma
    aksioma = "Total sudut segitiga adalah 180 derajat"
    print(f"Aksioma: {aksioma}")

    # Teorema
    teorema = "Segitiga siku-siku memiliki sudut 90 derajat"
    print(f"Teorema: {teorema}")

    # Lemma
    lemma = "Sudut di seberang sisi terpanjang dalam segitiga siku-siku adalah 90 derajat"
    print(f"Lemma: {lemma}")

    # Corollary
    corollary = "Jika segitiga memiliki sudut 90 derajat, maka segitiga tersebut adalah segitiga siku-siku"
    print(f"Corollary: {corollary}")
    print("===============================================\n")


if __name__ == "__main__":
    biconditional_logic_case()
    inference_case()
    argument_case()
    axioms_theorems_case()
