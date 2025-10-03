#CONDITIONAL AND LOGIC OPERATIONS

# 1. Check Odd or Even Number
print("========Check Odd or Even Number=======")
number = int(input("Enter a number: "))
if number % 2 == 1:
    print(f"The number {number} is odd")
else:
    print(f"The number {number} is even")

# 2. Check Exam Grade
print("========Check Exam Grade=======")
score = int(input("Enter your exam score (0-100): "))

if 90 <= score <= 100:
    print("Your grade is Excellent")
elif 80 <= score < 89:
    print("Your grade is Good")
elif 70 <= score < 79:
    print("Your grade is Fair")
elif 60 <= score < 69:
    print("Your grade is Poor")
elif 0 <= score < 59:
    print("Your grade is Very Poor")

# 3. Check Health Status
print("========Check Health Status=======")
age = int(input("Enter your age: "))
blood_pressure = int(input("Enter your blood pressure: "))

if age >= 60 and blood_pressure > 140:
    print("Health status is High")
elif age >= 60 and blood_pressure <= 140:
    print("Health status is Normal")
elif age < 60 and blood_pressure > 130:
    print("Health status is High")
elif age < 60 and blood_pressure <= 130:
    print("Health status is Normal")

# 4. Find Largest Number
print("========Find Largest Number=======")
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number1 > number2 and number1 > number3:
    print("The largest number is:", number1)
elif number2 > number3:
    print("The largest number is:", number2)
else:
    print("The largest number is:", number3)

print("--------------------------------------------------------------------------------------------------")
#LOOPING

# 1. Find Odd Numbers
print("=====Program to determine odd numbers====")
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print("Odd numbers between", start, "and", end, "are:")

while start <= end:
    if start % 2 != 0:
        print(start, end=' ')
    start += 1

# 2. Print Number Multiple Times
print("======Program to print a number as many times as the number entered========")
number = int(input("Enter a number: "))

i = 0
while i < number:
    print(number)
    i += 1

# 3. Calculate Average Grade
print("====Program to calculate the average grade of a number of students=====")
student_count = int(input("Enter the number of students: "))

i = 0
while i < student_count:
    print("===============================================")
    print(f"Student {i+1}")
    subject_count = int(input("Enter the number of subjects taken: "))
    
    total_score = 0  # reset for each student
    
    for j in range(subject_count):
        score = float(input(f"Enter the grade for subject {j+1}: "))
        total_score += score
    
    average = total_score / subject_count
    print(f"The average grade of Student {i+1} is: {average}")
    
    i += 1

print("Program finished. Thank you!")