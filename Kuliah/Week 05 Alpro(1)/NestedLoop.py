## NESTED LOOP (extended)
# (Similar to Github Repo: deenaariff)
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def _save_image_from_array(arr: np.ndarray, out_path: Path, mode: str):
    """
    Save a numpy array as an image with the given PIL mode.
    mode: "RGB" for color, "L" for grayscale/binary.
    """
    out_path = out_path.with_suffix(".png")
    Image.fromarray(arr, mode).save(out_path)
    print(f"Image saved as {out_path.name}")

def rgb_values():
    img = input("Enter image file name: ").strip()
    src_path = Path(img)
    image = Image.open(src_path).convert("RGB")
    arr = np.array(image, dtype=np.uint8)
    H, W, _ = arr.shape

    # preview
    plt.imshow(arr); plt.axis("off"); plt.title(f"Preview of {src_path.name}")
    ax = plt.gca()
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x)}"))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f"{int(y)}"))
    plt.show()

    # save RGB copy
    out_rgb = src_path.with_name(f"{src_path.stem}_rgb")
    _save_image_from_array(arr, out_rgb, mode="RGB")

    # CSV export
    yy, xx = np.indices((H, W), dtype=int)
    R = arr[:, :, 0].ravel(); G = arr[:, :, 1].ravel(); B = arr[:, :, 2].ravel()
    table = np.column_stack([xx.ravel(), yy.ravel(), R, G, B])
    header = "x,y,R,G,B"
    np.savetxt("rgb_values.csv", table, fmt="%d", delimiter=",", header=header, comments="")
    print("CSV saved as rgb_values.csv")

    # optional terminal print
    limit = int(input("How many pixels to print? (0 = all): ") or 0)
    total = H * W; count = 0
    print("\n--- RGB COORDINATES ---")
    for y in range(H):
        for x in range(W):
            r, g, b = arr[y, x]
            print(f"({x:3d},{y:3d}) → RGB({r},{g},{b})")
            count += 1
            if limit != 0 and count == limit:
                print("------- limit reached -------")
                return
    print(f"\nDone printing all {total} RGB coordinates.")

def grayscale():
    img = input("Enter image file name: ").strip()
    src_path = Path(img)
    image = Image.open(src_path).convert("RGB")
    arr = np.array(image, dtype=np.uint8)
    H, W, _ = arr.shape

    grey = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    grey_u8 = grey.clip(0, 255).astype(np.uint8)

    plt.imshow(grey_u8, cmap="gray"); plt.axis("off"); plt.title(f"Grayscale of {src_path.name}")
    ax = plt.gca()
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x)}"))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f"{int(y)}"))
    plt.show()

    out_gray = src_path.with_name(f"{src_path.stem}_grayscale")
    _save_image_from_array(grey_u8, out_gray, mode="L")

    yy, xx = np.indices((H, W), dtype=int)
    Grey = grey_u8.ravel()
    table = np.column_stack([xx.ravel(), yy.ravel(), Grey])
    header = "x,y,GrayValue"
    np.savetxt("grayscale.csv", table, fmt="%d", delimiter=",", header=header, comments="")
    print("CSV saved as grayscale.csv")

def binary():
    img = input("Enter image file name: ").strip()
    src_path = Path(img)
    image = Image.open(src_path).convert("RGB")
    arr = np.array(image, dtype=np.uint8)
    H, W, _ = arr.shape

    grey = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    try:
        threshold = int(input("Threshold (0-255, default 128): ") or 128)
    except ValueError:
        threshold = 128

    bw = np.where(grey >= threshold, 255, 0).astype(np.uint8)

    plt.imshow(bw, cmap="gray"); plt.axis("off"); plt.title(f"Binary (threshold {threshold}) of {src_path.name}")
    ax = plt.gca()
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x)}"))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f"{int(y)}"))
    plt.show()

    out_bw = src_path.with_name(f"{src_path.stem}_binary_t{threshold}")
    _save_image_from_array(bw, out_bw, mode="L")

    yy, xx = np.indices((H, W), dtype=int)
    table = np.column_stack([xx.ravel(), yy.ravel(), bw.ravel()])
    header = "x,y,BinaryValue"
    np.savetxt("binary.csv", table, fmt="%d", delimiter=",", header=header, comments="")
    print("CSV saved as binary.csv")

# NEW: High-Resolution Upscale with LANCZOS + optional sharpening
def high_resolution():
    img = input("Enter image file name: ").strip()
    src_path = Path(img)
    image = Image.open(src_path).convert("RGB")

    scale_or_size = input("Enter scale (e.g., 2) or size WxH (e.g., 1920x1080): ").lower().strip()
    if "x" in scale_or_size:
        try:
            w, h = map(int, scale_or_size.split("x"))
            new_w, new_h = w, h
            suffix = f"{w}x{h}"
        except Exception:
            print("Invalid size. Example: 1920x1080")
            return
    else:
        try:
            s = float(scale_or_size or "2")
            new_w = int(image.width * s)
            new_h = int(image.height * s)
            suffix = f"scale{s:g}"
        except ValueError:
            print("Invalid scale. Example: 2")
            return

    # LANCZOS upscaling
    up = image.resize((new_w, new_h), resample=Image.LANCZOS)

    # Optional: a touch of sharpening to restore perceived detail
    try:
        amount = float(input("Sharpen amount (0=none, 0.0-2.0, default 0.3): ") or 0.3)
    except ValueError:
        amount = 0.3
    if amount > 0:
        up = ImageEnhance.Sharpness(up).enhance(1 + amount)

    out_hr = src_path.with_name(f"{src_path.stem}_HR_{suffix}.png")
    up.save(out_hr, optimize=True)
    print(f"High-resolution image saved as {out_hr.name}")

    # Quick preview
    plt.imshow(np.asarray(up)); plt.axis("off"); plt.title(f"High-Res: {out_hr.name}")
    plt.show()

# NEW: Contour / Edge Map + red overlay
def contour_edges():
    img = input("Enter image file name: ").strip()
    src_path = Path(img)
    image = Image.open(src_path).convert("RGB")

    # Edge detection
    gray = ImageOps.grayscale(image)
    edges = gray.filter(ImageFilter.FIND_EDGES)
    edges = ImageOps.autocontrast(edges)  # pop the edges

    # Optional threshold to keep strong edges
    try:
        t = int(input("Edge threshold (0-255, default 20): ") or 20)
    except ValueError:
        t = 20
    edges_bin = edges.point(lambda p: 255 if p >= t else 0)  # 'L' 0/255

    # Save edge maps
    out_edges = src_path.with_name(f"{src_path.stem}_contour_edges.png")
    out_bin = src_path.with_name(f"{src_path.stem}_contour_thresh{t}.png")
    edges.save(out_edges); edges_bin.save(out_bin)
    print(f"Edge map saved as {out_edges.name}")
    print(f"Thresholded edge map saved as {out_bin.name}")

    # Red overlay on original (edges in red)
    red_layer = Image.new("RGB", image.size, (255, 0, 0))
    overlay = Image.composite(red_layer, image, edges_bin)
    out_overlay = src_path.with_name(f"{src_path.stem}_contour_overlay_t{t}.png")
    overlay.save(out_overlay)
    print(f"Overlay saved as {out_overlay.name}")

    # Preview
    fig = plt.figure(figsize=(10, 6))
    plt.imshow(np.asarray(overlay)); plt.axis("off")
    plt.title(f"Contour Overlay ({src_path.name}, t={t})")
    plt.show()

if __name__ == "__main__":
    print("Modes available:")
    print("1. Print coordinates and rgb codes")
    print("2. Convert to Grayscale")
    print("3. Convert to Binary (Black/White)")
    print("4. High-Resolution Upscale")
    print("5. Contour / Edge Map")
    choice = input("Choose mode (1/2/3/4/5 or rgb/grayscale/binary/highres/contour): ").strip().lower()

    if choice in ("1", "rgb"):
        rgb_values()
    elif choice in ("2", "grayscale"):
        grayscale()
    elif choice in ("3", "binary"):
        binary()
    elif choice in ("4", "highres", "high-resolution", "hr"):
        high_resolution()
    elif choice in ("5", "contour", "edges", "edge"):
        contour_edges()
    else:
        print("Invalid choice. Please choose 1–5.")
