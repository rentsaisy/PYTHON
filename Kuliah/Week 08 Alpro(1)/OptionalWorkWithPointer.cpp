#include <iostream>      // Untuk input-output standar
#include <fstream>       // Untuk membaca file
#include <iomanip>       // Untuk format hex (setw, setfill)
#include <sstream>       // Untuk mengubah hash menjadi string
#include <openssl/sha.h> // Library OpenSSL untuk fungsi SHA256
#include <sys/stat.h>    // Untuk mengambil informasi ukuran file

using namespace std;

// ============================================================================
// Fungsi: getFileSizeKB
// Deskripsi: Menghitung ukuran file dalam satuan kilobyte (KB)
// Parameter: pointer ke string (nama file)
// Return: double (ukuran file dalam KB)
// ============================================================================
double getFileSizeKB(const string* filenamePtr) {
    struct stat fileStat; // Struktur untuk menyimpan metadata file
    if (stat(filenamePtr->c_str(), &fileStat) != 0)
        return 0.0; // Jika gagal mengambil data file, kembalikan 0
    return static_cast<double>(fileStat.st_size) / 1024.0; // Byte → KB
}

// ============================================================================
// Fungsi: getFileChecksum
// Deskripsi: Menghasilkan checksum SHA-256 dari file menggunakan pointer
// Parameter: pointer ke string (nama file)
// Return: string (hash hasil SHA-256 dalam format heksadesimal)
// ============================================================================
string getFileChecksum(const string* filenamePtr) {
    // Membuka file dalam mode biner melalui pointer dinamis
    ifstream* file = new ifstream(filenamePtr->c_str(), ios::binary);
    if (!file->is_open()) {
        cerr << "[!] File '" << *filenamePtr << "' not found." << endl;
        delete file;
        return "";
    }

    // Inisialisasi konteks SHA256
    SHA256_CTX sha256;
    SHA256_Init(&sha256);

    // Alokasi buffer dinamis untuk membaca isi file
    const size_t bufferSize = 32768; // 32 KB per blok baca
    unsigned char* buffer = new unsigned char[bufferSize];

    // Membaca file secara bertahap dan memperbarui hash
    while (file->good()) {
        file->read(reinterpret_cast<char*>(buffer), bufferSize);
        SHA256_Update(&sha256, buffer, file->gcount()); // Update hash
    }

    // Alokasi memori untuk hasil akhir hash
    unsigned char* hash = new unsigned char[SHA256_DIGEST_LENGTH];
    SHA256_Final(hash, &sha256); // Ambil hasil hash

    // Mengubah hash (byte) menjadi string heksadesimal
    stringstream ss;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++)
        ss << hex << setw(2) << setfill('0') << (int)hash[i];

    // Bebaskan memori heap untuk menghindari memory leak
    delete[] buffer;
    delete[] hash;
    file->close();
    delete file;

    return ss.str(); // Kembalikan hash dalam bentuk string
}

// ============================================================================
// Fungsi Utama: main()
// Deskripsi: Mengontrol alur utama program (input, pemrosesan, dan output)
// ============================================================================
int main() {
    string file1, file2;

    // Input nama file dari pengguna
    cout << "Input the first file name: ";
    getline(cin, file1);
    cout << "Input the second file name: ";
    getline(cin, file2);

    // Buat pointer yang menunjuk ke variabel file
    string* ptrFile1 = &file1;
    string* ptrFile2 = &file2;

    // Hitung checksum masing-masing file
    string checksum1 = getFileChecksum(ptrFile1);
    string checksum2 = getFileChecksum(ptrFile2);

    // Jika kedua file valid dan hash berhasil dihitung
    if (!checksum1.empty() && !checksum2.empty()) {
        cout << "\n--- FILE DETAILS ---" << endl;
        cout << *ptrFile1 << " | Size: " << getFileSizeKB(ptrFile1) << " KB" << endl;
        cout << *ptrFile2 << " | Size: " << getFileSizeKB(ptrFile2) << " KB" << endl;

        cout << "\n--- SHA256 CHECKSUMS ---" << endl;
        cout << *ptrFile1 << ": " << checksum1 << endl;
        cout << *ptrFile2 << ": " << checksum2 << endl;

        cout << "\n--- RESULT ---" << endl;
        // Bandingkan hasil hash
        if (checksum1 == checksum2)
            cout << "The files are IDENTICAL (same content)." << endl;
        else
            cout << "The files are DIFFERENT." << endl;
    } 
    else {
        // Jika file tidak ditemukan
        cout << "\nProcess stopped due to missing file(s)." << endl;
    }

    return 0; // Program selesai
}
