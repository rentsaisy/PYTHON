def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def arithmetic_series(a, d, n):
    if n == 1:
        return a
    else:
        return a + arithmetic_series(a + d, d, n - 1)

def reverse_print(n):
    if n == 0:
        return
    print(n)
    reverse_print(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def digit_summation(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + digit_summation(n // 10)
    
def reverse_string(s):
    if s == "":
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
    
def exponentiation(a, b):
    if b == 0:
        return 1
    else:
        return a * exponentiation(a, b - 1)
    
def is_palindrome(teks):
    if len(teks) <= 1:
        return True
    elif teks[0] != teks[-1]:
        return False
    else:
        return is_palindrome(teks[1:-1])

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        tower_of_hanoi(n - 1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        tower_of_hanoi(n - 1, auxiliary, target, source)
        
def combination_or_permutation(n, r, is_permutation):
    def factorial_inner(x):
        if x == 0 or x == 1:
            return 1
        else:
            return x * factorial_inner(x - 1)
    
    if is_permutation:
        return factorial_inner(n) // factorial_inner(n - r)
    else:
        return factorial_inner(n) // (factorial_inner(r) * factorial_inner(n - r))

def main():
    while True:
        print("\n=== MENU REKURSI ===")
        print("1. Faktorial")
        print("2. Arithmetic Series")
        print("3. Reverse Print")
        print("4. Fibonacci")
        print("5. Digit Summation")
        print("6. Reverse String")
        print("7. Exponentiation")
        print("8. Palindrome Check")
        print("9. Tower of Hanoi")
        print("10. Combination/Permutation")
        print("0. Keluar")
        
        choice = input("Pilih menu (0-9): ")
        
        if choice == "1":
            n = int(input("Masukkan angka untuk faktorial: "))
            print(f"Hasil: {factorial(n)}")
            
        elif choice == "2":
            a = int(input("Masukkan suku pertama: "))
            d = int(input("Masukkan beda (d): "))
            n = int(input("Masukkan jumlah suku: "))
            print(f"Hasil: {arithmetic_series(a, d, n)}")
            
        elif choice == "3":
            n = int(input("Masukkan angka untuk dicetak mundur: "))
            reverse_print(n)
            
        elif choice == "4":
            n = int(input("Masukkan indeks Fibonacci: "))
            print(f"Hasil: {fibonacci(n)}")
            
        elif choice == "5":
            n = int(input("Masukkan angka untuk jumlah digit: "))
            print(f"Hasil: {digit_summation(n)}")
            
        elif choice == "6":
            s = input("Masukkan string: ")
            print(f"Hasil: {reverse_string(s)}")
            
        elif choice == "7":
            a = int(input("Masukkan basis (a): "))
            b = int(input("Masukkan pangkat (b): "))
            print(f"Hasil: {exponentiation(a, b)}")
            
        elif choice == "8":
            teks = input("Masukkan string untuk dicek palindrome: ")
            if is_palindrome(teks):
                print(f"{teks} adalah palindrome")
            else:
                print(f"{teks} bukan palindrome")
                
        elif choice == "9":
            n = int(input("Masukkan jumlah disk: "))
            tower_of_hanoi(n, "A", "B", "C")
            
        elif choice == "10":
            n = int(input("Masukkan n: "))
            r = int(input("Masukkan r: "))
            tipe = input("Ketik 'p' untuk permutasi atau 'c' untuk kombinasi: ").lower()
            is_permutation = tipe == 'p'
            print(f"Hasil: {combination_or_permutation(n, r, is_permutation)}")
            
        elif choice == "0":
            print("Keluar program...")
            break
            
        else:
            print("Pilihan tidak valid! Silakan pilih 0-9.")

if __name__ == "__main__":
    main()