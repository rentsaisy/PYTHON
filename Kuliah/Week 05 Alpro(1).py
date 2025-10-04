## FUNCTION

# 1. Function with no return
def message():
    print("Welcome to the Python program!")

message()
print("-----------------------------------------------------")

# 2. Function with return
def divide(a, b):
    return a / b

print("The result of dividing 10 and 2 is", divide(10, 2))
print("-----------------------------------------------------")

# 3. Function with default argument
def greeting(name, message="Happy birthday!"):
    print(f"Hello {name}, {message}")
    
greeting("Budi")
greeting("Karin", "Wish you great success always!")
print("-----------------------------------------------------")

# 4. Function with variable-length arguments
def subtract(*numbers):
    result = numbers[0]  # start from the first number
    for i in numbers[1:]:
        result -= i
    return result

print("The subtraction of 10-20-30 is", subtract(10, 20, 30))  # Output: -40
print("The subtraction of 5-15 is", subtract(5, 15))           # Output: -10
print("-----------------------------------------------------")

# 5. Function with keyword variable-length arguments
def biodata(**info):
    for key, value in info.items():
        print(f"{key} : {value}")

biodata(name="Aisyah", age=19, major="Informatics Management")

##NESTED LOOP
# 1. Nested loop to print coordinates and RGB values of an image
from PIL import Image       
import numpy as np          
import pandas as pd         

image = Image.open("yoyo.jpg")     
image = image.resize((250, 250))  

array_image = np.array(image)

R = array_image[:, :, 0]  
G = array_image[:, :, 1]
B = array_image[:, :, 2]

rgb_data = []   

for y in range(image.height):     
    for x in range(image.width):   
        r = R[y, x]
        g = G[y, x]
        b = B[y, x]
        
        rgb_data.append([x, y, r, g, b])

rgb_table = pd.DataFrame(rgb_data, columns=["X", "Y", "R", "G", "B"])

rgb_table.to_csv("rgb.csv", index=False)

print("RGB data is in 'rgb.csv'")
print("Here are the first 5 entries:")
print(rgb_table.head())
print("-----------------------------------------------------")

# 2. Nested loop to Grayscale       
from PIL import Image
import numpy as np
import pandas as pd

image = Image.open("yoyo.jpg")     
image = image.resize((250, 250))   

grayscale_array = np.zeros((image.height, image.width), dtype=np.uint8)

for y in range(image.height):
    for x in range(image.width):
        grayscale_array[y, x] = int((R[y, x] + G[y, x] + B[y, x]) / 3)

grayscale_image = Image.fromarray(grayscale_array, mode="L")
grayscale_image.show()
grayscale_image.save("grayscale_result.jpg")

print("The image has been successfully converted to grayscale and saved as 'grayscale_result.jpg'")
print("-----------------------------------------------------")

#(Similar to Github Repo:deenaariff)
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open image and ensure RGB
image = Image.open("yoyo.jpg").convert("RGB")

# Convert to numpy array: shape (H, W, 3)
arr = np.array(image)
H, W, _ = arr.shape

# Initialize grayscale arrays
grey  = np.zeros((H, W), dtype=np.float32)  # human-weighted
grey2 = np.zeros((H, W), dtype=np.float32)  # raw average

# 'Human' luminance (no /3)
def average1(pixel):
    return 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]

# Raw average
def average2(pixel):
    return np.average(pixel)

# Map averages of pixels to the grey images (nested loops)
for r in range(H):
    for c in range(W):
        p = arr[r, c]                 # [R, G, B]
        grey[r, c]  = average1(p)
        grey2[r, c] = average2(p)

# Convert to 8-bit for display/saving
grey_u8  = grey.clip(0, 255).astype(np.uint8)
grey2_u8 = grey2.clip(0, 255).astype(np.uint8)

# Show one of them (human-weighted)
plt.imshow(grey_u8, cmap="gray")
plt.axis("off")
plt.show()

# (Optional) save results
Image.fromarray(grey_u8,  mode="L").save("grayscale_human.jpg")
Image.fromarray(grey2_u8, mode="L").save("grayscale_avg.jpg")

# 3. Nested loop to black and white
from PIL import Image
import numpy as np

image = Image.open("yoyo.jpg")
image = image.resize((250, 250))  

image_array = np.array(image)

R = image_array[:, :, 0]   
G = image_array[:, :, 1]  
B = image_array[:, :, 2]  

threshold = 128

brightness = (0.299 * R) + (0.587 * G) + (0.114 * B)

bw_array = np.where(brightness >= threshold, 255, 0).astype(np.uint8)

bw_image = Image.fromarray(bw_array, mode="L")

bw_image.show()
bw_image.save("black_white_result.jpg")

print("The image has been successfully converted to black and white!")
