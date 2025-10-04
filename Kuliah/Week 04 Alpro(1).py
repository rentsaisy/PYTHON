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