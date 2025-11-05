import hashlib  # Modul bawaan Python untuk menghasilkan hash (termasuk SHA256)
import os       # Modul untuk berinteraksi dengan sistem file

# ===============================================================
# Fungsi: get_file_checksum
# Deskripsi:
#   Menghitung nilai checksum SHA-256 dari file yang diberikan.
#   Fungsi ini memastikan bahwa isi file dibaca dalam mode biner
#   agar perhitungan hash akurat.
# Parameter:
#   filename (str) → Nama file yang akan dihitung hash-nya.
# Return:
#   String berisi hash SHA256 dalam format heksadesimal (64 karakter).
# ===============================================================
def get_file_checksum(filename):
    try:
        # Membuka file dalam mode biner (binary read)
        with open(filename, "rb") as f:
            file_data = f.read()  # Membaca seluruh isi file
            # Menghitung hash SHA-256 dari data file
            sha256_hash = hashlib.sha256(file_data).hexdigest()
            return sha256_hash  # Mengembalikan nilai hash heksadesimal
    except FileNotFoundError:
        # Jika file tidak ditemukan, tampilkan pesan kesalahan
        print(f"[!] File '{filename}' not found.")
        return None  # Kembalikan None untuk menandai error

# ===============================================================
# Fungsi: get_file_info
# Deskripsi:
#   Mengambil ukuran file dalam satuan kilobyte (KB).
# Parameter:
#   filename (str) → Nama file yang akan dicek.
# Return:
#   Ukuran file dalam KB (float). Jika tidak ada, kembalikan 0.
# ===============================================================
def get_file_info(filename):
    # Mengecek apakah file benar-benar ada
    if not os.path.isfile(filename):
        return 0
    # Jika ada, ambil ukuran file dalam byte dan ubah menjadi KB
    return os.path.getsize(filename) / 1024

# ===============================================================
# Fungsi Utama: main
# Deskripsi:
#   Mengatur alur utama program:
#   1. Meminta dua nama file dari pengguna
#   2. Menghitung hash SHA-256 untuk masing-masing file
#   3. Menampilkan ukuran, hash, dan hasil perbandingan
# ===============================================================
def main():
    # Meminta input nama dua file dari pengguna
    file1 = input("Input the first file name: ").strip()
    file2 = input("Input the second file name: ").strip()

    # Menghitung checksum SHA256 dari kedua file
    checksum1 = get_file_checksum(file1)
    checksum2 = get_file_checksum(file2)

    # Jika kedua file ditemukan dan hash berhasil dihitung
    if checksum1 and checksum2:
        print("\n--- FILE DETAILS ---")
        print(f"{file1} | Size: {get_file_info(file1)} KB")
        print(f"{file2} | Size: {get_file_info(file2)} KB")

        print("\n--- SHA256 CHECKSUMS ---")
        print(f"{file1}: {checksum1}")
        print(f"{file2}: {checksum2}")

        print("\n--- RESULT ---")
        # Membandingkan hasil hash untuk menentukan kesamaan isi file
        if checksum1 == checksum2:
            print("The files are IDENTICAL (same content).")
        else:
            print("The files are DIFFERENT.")
    else:
        # Jika salah satu file tidak ditemukan
        print("\nProcess stopped due to missing file(s).")

# ===============================================================
# Bagian utama program
# Deskripsi:
#   Memastikan fungsi main() hanya dijalankan jika file ini
#   dijalankan langsung (bukan diimpor sebagai modul).
# ===============================================================
if __name__ == "__main__":
    main()
