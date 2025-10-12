import hashlib
import os

def get_file_checksum(filename):
    try:
        with open(filename, "rb") as f:
            file_data = f.read()
            sha256_hash = hashlib.sha256(file_data).hexdigest()
            return sha256_hash
    except FileNotFoundError:
        print(f"[!] File '{filename}' not found.")
        return None

def get_file_info(filename):
    if not os.path.isfile(filename):
            return 0
    return os.path.getsize(filename) / 1024 
    
def main():
    file1 = input("Input the first file name: ").strip()
    file2 = input("Input the second file name: ").strip()

    checksum1 = get_file_checksum(file1)
    checksum2 = get_file_checksum(file2)

    if checksum1 and checksum2:
        print("\n--- FILE DETAILS ---")
        print(f"{file1} | Size: {get_file_info(file1)} KB")
        print(f"{file2} | Size: {get_file_info(file2)} KB")

        print("\n--- SHA256 CHECKSUMS ---")
        print(f"{file1}: {checksum1}")
        print(f"{file2}: {checksum2}")

        print("\n--- RESULT ---")
        if checksum1 == checksum2:
            print("The files are IDENTICAL (same content).")
        else:
            print("The files are DIFFERENT.")
    else:
        print("\nProcess stopped due to missing file(s).")

if __name__ == "__main__":
    main()