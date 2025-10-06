## 10 STUDY CASE
# 1. Determine if a number is positive, negative, or zero
print("=======Program to determine if a number is positive, negative, or zero=======")
number = int(input("Input a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 2. Determine the grade based on the score
print("=======Program to determine the grade based on the score=======")
score = int(input("Input the score (0-100): "))
if score >= 85 and score <= 100:
    print("Grade: A")
elif score >= 70 and score <= 84:
    print("Grade: B")
elif score >= 55 and score <= 69:
    print("Grade: C")
elif score >= 40 and score <= 54:
    print("Grade: D")
elif score >= 0 and score <= 39:
    print("Grade: E")
else:
    print("Invalid score input.")

# 3. Determine the day of the week based on the number
print("=======Program to determine the day of the week based on the number=======")
day = int(input("Input a number (1-7): "))

if day == 1:
    
    print("Day 1 is Sunday")
elif day == 2:
    print("Day 2 is Monday")
elif day == 3:
    print("Day 3 is Tuesday")
elif day == 4:
    print("Day 4 is Wednesday")
elif day == 5:
    print("Day 5 is Thursday")
elif day == 6:
    print("Day 6 is Friday")
elif day == 7:
    print("Day 7 is Saturday")
else:
    print("Input a valid number (1-7)")
    
# 4. Print numbers from 1 to the input number
print("=======Program to print numbers from 1 to the input number=======")
number = int(input("Input a number: "))

i = 1
while i <= number:
    print(i)
    i += 1

# 5.
N = int(input("Input a number: "))

i = 1
total = 0
while i <= N:
    if i % 2 == 1:
        print(i)
        total += i
    i += 1
print("Jumlah angka ganjil dari 1 sampai ", N, "is ", total) 