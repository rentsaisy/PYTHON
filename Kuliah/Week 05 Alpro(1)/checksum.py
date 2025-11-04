import hashlib
from pathlib import Path

def get_file_checksum(filename):
    path = Path(filename)
    if not path.is_file():
        print(f"[!] File '{filename}' not found.")
        return None

    with path.open("rb") as f:
        file_data = f.read()
    return hashlib.sha256(file_data).hexdigest()

def main():
    file = input("Enter file name (with extension): ").strip()
    checksum = get_file_checksum(file)

    if checksum:
        print(f"SHA-256 checksum for '{file}':")
        print(checksum)
    else:
        print("Failed to retrieve checksum.")

if __name__ == "__main__":
    main()
