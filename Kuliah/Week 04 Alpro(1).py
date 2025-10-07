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

# 5. Sum of odd numbers from 1 to N
print("=======Program to calculate the sum of odd numbers from 1 to N=======")
N = int(input("Input a number: "))

i = 1
total = 0
while i <= N:
    if i % 2 == 1:
        print(i)
        total += i
    i += 1
print("Sum of odd numbers from 1 to ", N, "is ", total)

# 6. Multiplication table of N
print("=======Program to print the multiplication table of N=======")
N = int(input("Input a number: "))

table = 1
while table <= 10: 
    result = N * table
    print(N, "x", table, "=", result)
    table += 1

# 7.
Bilangan = int(input("Masukkan sebuah angka: "))

i = 2
is_prime = True
while i <= Bilangan // 2:
    if Bilangan % i == 0:
        is_prime = False
        break
    i += 1
if is_prime and Bilangan > 1:
    print(Bilangan, "adalah bilangan prima.")
else:
    print(Bilangan, "bukan bilangan prima.")

# 8.
N = int(input("Masukkan tinggi pola segitiga bintang: "))
i = 1
while i <= N:
    print("*" * i)
    i += 1

# 9.
secret_number = 50
round = 0
round_limit = 8
print("============WELCOME TO GUESS THE NUMBER GAME============")
print("Your Round is " + str(round_limit))

while(round < round_limit):
    guess = int(input("Your guess:"))
    round += 1
    if (guess < secret_number):
        print ("Your guess is too low")
    elif (guess > secret_number):
        print ("Your guess is too high")
    else:
        print ("Congratulations! your guess is correct")
        exit(0)
    print("Your left round is " + str(round_limit - round))
while(round > round_limit):
        print("you're out of rounds, the secret number was " + str(secret_number))
        break
    
# 10.
print("Selamat datang! Silakan login.")
username = input("Username: ")
password = input("Password: ")
loginchance = 3
while True:
    if username == "admin" and password == "1234":
        print("Login berhasil! Selamat datang, " + username + ".")
        break
    else:
        loginchance -= 1
        if loginchance > 0:
            print("Akses gagal! Username atau password salah. Sisa kesempatan: " + str(loginchance))
            username = input("Username: ")
            password = input("Password: ")
        else:
            print("Akses ditolak! Kesempatan login habis.") 