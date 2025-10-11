import csv
import hashlib
import numpy as np
from PIL import Image

def hash_csv(csv_path):
    pixels = []
    with open(csv_path, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or row[0].startswith("#"):
                continue
            x, y, r, g, b = map(int, row[:5])
            pixels.append((x, y, r, g, b))

    width = max(p[0] for p in pixels) + 1
    height = max(p[1] for p in pixels) + 1
    arr = np.zeros((height, width, 3), dtype=np.uint8)

    for x, y, r, g, b in pixels:
        arr[y, x] = (r, g, b)

    return hashlib.sha256(arr.tobytes()).hexdigest(), arr.shape

def hash_image(img_path):
    img = Image.open(img_path).convert("RGB")
    arr = np.array(img, dtype=np.uint8)
    return hashlib.sha256(arr.tobytes()).hexdigest(), arr.shape

def compare_csv_and_image(csv_path, img_path):
    csv_hash, csv_shape = hash_csv(csv_path)
    img_hash, img_shape = hash_image(img_path)

    if csv_shape != img_shape:
        print("Different size:", csv_shape, "vs", img_shape)
        return False

    if csv_hash == img_hash:
        print("✅ CSV and image are identical!")
        return True
    else:
        print("❌ CSV and image differ.")
        print("CSV hash:", csv_hash)
        print("IMG hash:", img_hash)
        return False

compare_csv_and_image("pixels.csv", "picture.png")
