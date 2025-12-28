def convertToFahrenheit(degreeCelcius):
    return degreeCelcius * (9/5) + 32

def convertToCelcius(degreeFahrenheit):
    return (degreeFahrenheit - 32) * (5/9)

def main():
    print("Choose your option:\n 1. Convert Celcius to Fahrenheit\n 2. Convert Fahrenheit to Celcius\n")
    choose = int(input("Your option is: "))
    if choose == 1:
        degreeCelcius = int(input("Input your Celcius degree: "))
        print(f"The result: {convertToFahrenheit(degreeCelcius)} Fahrenheit")
        print("=========================================================")
        main()
    elif choose == 2:
        degreeFahrenheit = int(input("Input your Fahrenheit degree: "))
        print(f"The result: {convertToCelcius(degreeFahrenheit)} Celcius")
        print("=========================================================")
        main()
    else:
        print("Your input is invalid, please choose 1 or 2")
        print("=========================================================")
        main()
        
if __name__ == "__main__" :
    main()