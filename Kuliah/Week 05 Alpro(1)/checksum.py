import hashlib

def get_file_checksum(filename):
    with open(filename, "rb") as f:
        file_data = f.read()
        sha256_hash = hashlib.sha256()
        sha256_hash.update(file_data)
        return sha256_hash.hexdigest()
    
file1 = input("Input the first file name: ")
file2 = input("Input the second file name: ")

checksum1 = get_file_checksum(file1)
checksum2 = get_file_checksum(file2)

print(f"SHA256 Checksum 1: {checksum1}")
print(f"SHA256 Checksum 2: {checksum2}")

if checksum1 == checksum2:
    print("The files are identical.")
else:
    print("The files are different.")