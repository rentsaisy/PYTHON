def area(lenght, width):
    return lenght * width

def perimeter(lenght, width):
    return (lenght + width) * 2

def volume(lenght, width, height):
    return lenght * width * height

def surfaceArea(lenght, width, height):
    return ((lenght * width) + (lenght * height) + (width * height)) * 2

def main():
    print(" Here are straightforward calculations:\n 1. Area\n 2. Perimeter\n 3. Volume\n 2. Surface Area\n")
    choose = int(input("Your option is: "))
    if choose == 1:
        lenght = int(input("Input the lenght: "))
        width = int(input("Input the width: "))
        print(f"The result of Area: {area(lenght, width)}")
        print("=========================================================")
        main()
    elif choose == 2:
        lenght = int(input("Input the lenght: "))
        width = int(input("Input the width: "))
        print(f"The result of Perimeter: {perimeter(lenght, width)}")
        print("=========================================================")
        main()
    elif choose == 3:
        lenght = int(input("Input the lenght: "))
        width = int(input("Input the width: "))
        height = int(input("Input the height: "))
        print(f"The result of Volume: {volume(lenght, width, height)}")
        print("=========================================================")
        main()
    elif choose == 4:
        lenght = int(input("Input the lenght: "))
        width = int(input("Input the width: "))
        height = int(input("Input the height: "))
        print(f"The result of Surface Area: {surfaceArea(lenght, width, height)}")
        print("=========================================================")
        main()
    else:
        print("Your input is invalid, please choose 1 - 4")
        print("=========================================================")
        main()
        
if __name__ == "__main__" :
    main()