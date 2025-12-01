with open("story.txt", "r") as f:
    isi = f.readlines()

for baris in isi:
    print(baris.strip())