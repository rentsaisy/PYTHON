from PIL import Image
import csv
import time

def load_image(path):
    """Load image and convert to RGBA."""
    try:
        start_time = time.time()
        img = Image.open(path).convert("RGBA")
        end_time = time.time()

        print(f"Image loaded: {path}")
        print(f"Image size: {img.width}x{img.height} pixels")
        print(f"Image load time: {end_time - start_time:.4f} seconds")
        return img
    except FileNotFoundError:
        print("Image not found.")
        return None

def save_rgba_to_csv(img, output_csv):
    """Save all pixel coordinates and RGBA values to CSV."""
    if img is None:
        print("No image to process.")
        return

    start_time = time.time()
    with open(output_csv, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["x", "y", "R", "G", "B", "A"])  # Header

        for y in range(img.height):
            for x in range(img.width):
                r, g, b, a = img.getpixel((x, y))
                writer.writerow([x, y, r, g, b, a])
                # print(f"({x}, {y}) → R:{r}, G:{g}, B:{b}, A:{a}")  # optional

    end_time = time.time()
    print(f"\nRGBA data successfully saved to: {output_csv}")
    print(f"Processing time: {end_time - start_time:.4f} seconds")

def main():
    """Main program."""
    total_start = time.time()
    path = input("Enter image filename: ").strip()
    output_csv = input("Enter output CSV filename: ").strip()
    
    img = load_image(path)
    if img:
        save_rgba_to_csv(img, output_csv)
    total_end = time.time()
    print(f"\nTotal execution time: {total_end - total_start:.4f} seconds")

if __name__ == "__main__":
    main()
