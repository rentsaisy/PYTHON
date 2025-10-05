from PIL import Image
from pathlib import Path

def open_image_anywhere(filename: str) -> Image.Image:
    p = Path(filename)
    if not p.is_file():
        p = Path(__file__).parent / filename
    if not p.is_file():
        raise FileNotFoundError(f"Tidak menemukan file: {filename}\nDicoba di: {Path.cwd()} dan {Path(__file__).parent}")
    return Image.open(p).convert("RGBA")

def printRGBValues():
    inputImage = input("Please input image name including its extension: ")
    openImage = open_image_anywhere(inputImage)
    pixels = openImage.load()

    width, height = openImage.size
    print(f"Image size: {width}x{height}")
    print("Showing RGB(A) values (may be long for big images):\n")

    limit = int(input("How many pixels to print (0 = all)? "))
    count = 0

    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            print(f"({x},{y}) -> R:{r} G:{g} B:{b} A:{a}")
            count += 1
            if limit != 0 and count >= limit:
                print("\n--- Limit reached ---")
                return
    print("\nFinished printing all RGB(A) values!")

def extractValueGrayscale():
    """Convert to grayscale and save to CSV."""
    inputImage = input("Please input image name including its extension: ")
    openImage = open_image_anywhere(inputImage)
    pixels = openImage.load()
    width, height = openImage.size

    gray_img = Image.new("L", (width, height))
    
    with open("extracted_value.csv", "w", encoding="utf-8") as f:
        for y in range(height):
            for x in range(width):
                r, g, b, a = pixels[x, y]
                gray = int(0.299*r + 0.587*g + 0.114*b)
                f.write(f"{gray},{gray},{gray},{a}\n")
                gray_img.putpixel((x, y), gray)
                
    gray_img.save("grayscale_result.png")
    print("Process completed! Grayscale values saved to extracted_value.csv")

def extractValueBinary():
    """Convert to black/white and save to CSV."""
    inputImage = input("Please input image name including its extension: ")
    openImage = open_image_anywhere(inputImage)
    pixels = openImage.load()
    width, height = openImage.size
    
    binary_img = Image.new("L", (width, height))

    with open("extracted_value.csv", "w", encoding="utf-8") as f:
        for y in range(height):
            for x in range(width):
                r, g, b, a = pixels[x, y]
                gray = int(0.299*r + 0.587*g + 0.114*b)
                bw = 255 if gray >= 128 else 0
                f.write(f"{bw},{bw},{bw},{a}\n")
                binary_img.putpixel((x, y), bw)
    
    binary_img.save("binary_result.png")
    print("Process completed! Binary values saved to extracted_value.csv")
    
if __name__ == "_main_":
    print("Modes available: grayscale | binary | print rgb")
    choice = input("Choose mode (print rgb or grayscale or binary): ").strip().lower()

    if choice == "print rgb":
        printRGBValues()
    elif choice == "grayscale":
        extractValueGrayscale()
    elif choice == "binary":
        extractValueBinary()
    else:
        print("Invalid choice. Please choose 'print RGB' or 'grayscale' or 'binary'.")