# Number 1
# Algorithm for Calculating the Area of a Triangle

print("Calculating Triangle Area")

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = 0.5 * base * height

print(f"The area of the triangle is {area}")

# Number 2
# 1. Start
# 2. Input the base and height
# 3. Calculate the area using the formula:
#    Area = 0.5 * base * height
# 4. Display the area
# 5. End

def calculate_triangle_area(base, height):
    return 0.5 * base * height

print("Triangle Area Program")
base = float(input("Enter the base: "))
height = float(input("Enter the height: "))
print(f"Triangle area: {calculate_triangle_area(base, height)}")

# Number 3
# Example 1
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b and a > c:
    print(f"The largest number is {a}")
elif b > c:
    print(f"The largest number is {b}")
else:
    print(f"The largest number is {c}")

# Example 2
n = int(input("Enter a number n: "))
total = sum(range(1, n + 1))
print(f"The sum of numbers from 1 to {n} is {total}")

# Number 4
n = int(input("Enter an integer: "))

if n % 2 == 0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")

