##NESTED LOOP
#(Similar to Github Repo:deenaariff)
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def open_image_anywhere(filename: str) -> Image.Image:
    p = Path(filename)
    if not p.is_file():
        p = Path(__file__).parent / filename
    if not p.is_file():
        raise FileNotFoundError(f"Tidak menemukan file: {filename}\nDicoba di: {Path.cwd()} dan {Path(__file__).parent}")
    return Image.open(p).resize((250, 250)).convert("RGB")

def rgb_values():
    img = input("Enter image file name: ").strip()
    image = open_image_anywhere(img)
    arr = np.array(image, dtype=np.uint8)
    H, W, _ = arr.shape

    plt.imshow(arr)
    plt.axis("off")
    plt.title(f"Preview of {img}")
    ax = plt.gca()
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x)}"))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f"{int(y)}"))
    plt.show()

    yy, xx = np.indices((H, W), dtype=int)
    R = arr[:, :, 0].ravel()
    G = arr[:, :, 1].ravel()
    B = arr[:, :, 2].ravel()

    table = np.column_stack([xx.ravel(), yy.ravel(), R, G, B])
    header = "x,y,R,G,B"

    np.savetxt("rgb_values.csv", table, fmt="%d", delimiter=",", header=header, comments="")
    print("CSV saved as rgb_values.csv")

    limit = int(input("How many pixels to print? (0 = all): ") or 0)
    total = H * W
    count = 0

    print("\n--- RGB COORDINATES ---")
    for y in range(H):
        for x in range(W):
            r, g, b = arr[y, x]
            print(f"({x:3d},{y:3d}) → RGB({r},{g},{b})")
            count += 1
            if limit != 0 and count == limit:
                print(f"------- limit reached -------")
                return

    print(f"\n Done printing all {total} RGB coordinates.")

def grayscale():
    img = input("Enter image file name: ").strip()
    image = open_image_anywhere(img)
    arr = np.array(image, dtype=np.uint8)
    H, W, _ = arr.shape

    grey = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]

    grey_u8 = grey.clip(0, 255).astype(np.uint8)
    plt.imshow(grey_u8, cmap="gray")
    plt.axis("off")
    plt.title(f"Grayscale of {img}")
    ax = plt.gca()
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x)}"))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f"{int(y)}"))
    plt.show()

    yy, xx = np.indices((H, W), dtype=int)
    Grey = grey_u8.ravel()
    table = np.column_stack([xx.ravel(), yy.ravel(), Grey])
    header = "x,y,GrayValue"
    np.savetxt("grayscale.csv", table, fmt="%d", delimiter=",", header=header, comments="")
    print("CSV saved as grayscale.csv")

def binary():
    img = input("Enter image file name: ").strip()
    image = open_image_anywhere(img)
    arr = np.array(image, dtype=np.uint8)
    H, W, _ = arr.shape

    grey = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]

    threshold = 128
    bw = np.where(grey >= threshold, 255, 0).astype(np.uint8)

    plt.imshow(bw, cmap="gray")
    plt.axis("off")
    plt.title(f"Binary (threshold {threshold}) of {img}")
    ax = plt.gca()
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x)}"))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f"{int(y)}"))
    plt.show()

    yy, xx = np.indices((H, W), dtype=int)
    table = np.column_stack([xx.ravel(), yy.ravel(), bw.ravel()])
    header = "x,y,BinaryValue"
    np.savetxt("binary.csv", table, fmt="%d", delimiter=",", header=header, comments="")
    print("CSV saved as binary.csv")

if __name__ == "__main__":
    print("Modes available:")
    print("1. Print coordinates and rgb codes")
    print("2. Convert to Grayscale")
    print("3. Convert to Binary (Black/White)")
    choice = input("Choose mode (1/2/3) or (rgb/grayscale/binary): ").strip()

    if choice == "1" or choice.lower() == "rgb":
        rgb_values()
    elif choice == "2" or choice.lower() == "grayscale":
        grayscale()
    elif choice == "3" or choice.lower() == "binary":
        binary()
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")