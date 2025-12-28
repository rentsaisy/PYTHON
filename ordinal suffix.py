def ordinalSuffix(number):
    if number % 100 in (11, 12, 13):
        return str(number) + 'th'
    if number % 10 == 1 :
        return str(number) + 'st'
    if number % 10 == 2 :
        return str(number) + 'nd'
    if number % 10 == 3:
        return str(number) + 'rd'
    return str(number) + 'th'

def checkfunc():
    assert ordinalSuffix(0) == '0th' 
    assert ordinalSuffix(1) == '1st' 
    assert ordinalSuffix(2) == '2nd' 
    assert ordinalSuffix(3) == '3rd' 
    assert ordinalSuffix(4) == '4th' 
    assert ordinalSuffix(10) == '10th' 
    assert ordinalSuffix(11) == '11th' 
    assert ordinalSuffix(12) == '12th' 
    assert ordinalSuffix(13) == '13th' 
    assert ordinalSuffix(14) == '14th' 
    assert ordinalSuffix(101) == '101st'
    print("The functions is working!\n")
    
def main():
    checkfunc()
    number = int(input("Please input a number: "))
    print(f"The ordinal suffix of the number is {ordinalSuffix(number)}")
    print("===================================================")
    main()
    
if __name__ == '__main__':
    main()