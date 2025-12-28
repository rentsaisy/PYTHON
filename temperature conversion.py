def convertToFahrenheit(degreeCelcius):
    return degreeCelcius * (9/5) + 32

def convertToCelsius(degreeFahrenheit):
    return (degreeFahrenheit - 32) * (5/9)

def checkfunc():
    assert convertToCelsius(0) == -17.77777777777778 
    assert convertToCelsius(180) == 82.22222222222223 
    assert convertToFahrenheit(0) == 32 
    assert convertToFahrenheit(100) == 212 
    assert convertToCelsius(convertToFahrenheit(15)) == 15 
    # Rounding errors cause a slight discrepancy: 
    assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001 
    print("The functions is working!\n")

def main():
    checkfunc()
    print("Choose your option:\n 1. Convert Celcius to Fahrenheit\n 2. Convert Fahrenheit to Celcius\n")
    choose = int(input("Your option is: "))
    if choose == 1:
        degreeCelcius = int(input("Input your Celcius degree: "))
        print(f"The result: {convertToFahrenheit(degreeCelcius)} Fahrenheit")
        print("=========================================================")
        main()
    elif choose == 2:
        degreeFahrenheit = int(input("Input your Fahrenheit degree: "))
        print(f"The result: {convertToCelsius(degreeFahrenheit)} Celsius")
        print("=========================================================")
        main()
    else:
        print("Your input is invalid, please choose 1 or 2")
        print("=========================================================")
        main()
        
if __name__ == "__main__" :
    main()