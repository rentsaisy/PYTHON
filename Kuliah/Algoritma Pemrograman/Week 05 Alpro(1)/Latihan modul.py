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
