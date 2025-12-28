def fizzBuzz(upTo):
    for number in range (1, upTo + 1):
        if number % 3 == 0 and number % 5 == 0:
            print(" FizzBuzz,", end=' ')
        elif number % 3 == 0:
            print(" Fizz,", end=' ')
        elif number % 5 == 0:
            print(" Buzz,", end=' ')
        elif number == upTo:
            print(f"{upTo}", end=' ')
        else:
            print(f" {number},", end='')

def main():
    upTo = (int(input("Let's Play FizzBuzz!\n input your up to number: ")))
    print("The result:")
    fizzBuzz(upTo)

if __name__ == '__main__' :
    main()