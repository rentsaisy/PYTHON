def isOdd(n):
    return n % 2 == 1

def isEven(n):
    return n % 2 == 0

def checkfunc():
    assert isOdd(42) == False 
    assert isOdd(9999) == True 
    assert isOdd(-10) == False 
    assert isOdd(-11) == True 
    assert isOdd(3.1415) == False 
    assert isEven(42) == True 
    assert isEven(9999) == False 
    assert isEven(-10) == True 
    assert isEven(-11) == False 
    assert isEven(3.1415) == False
    print("The functions is working!\n")

def main():
    checkfunc()
    n = float(input("Input a number: "))
    
    if isOdd(n) == True:
        print(f"The result: {n} is an Odd number")
        print("=========================================================")
        main()
    elif isEven(n) == True:
        print(f"The result: {n} is an Even number")
        print("=========================================================")
        main()
    else:
        print("Your input is invalid")
        print("=========================================================")
        main()
        
if __name__ == "__main__" :
    main()