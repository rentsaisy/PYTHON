def main(): # Main procedure starts here
    print('Please enter 10 different numbers below... ') 
    
    # Input 10 numbers
    numbers = []
    for i in range(10):
        num = int(input(f'Number {i+1}: '))
        numbers.append(num)
    
    # Calculate mean
    Mean = sum(numbers) / len(numbers)
    
    # Sort the numbers using bubble sort
    sorted_numbers = numbers.copy()
    n = len(sorted_numbers)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_numbers[j] > sorted_numbers[j+1]:
                sorted_numbers[j], sorted_numbers[j+1] = sorted_numbers[j+1], sorted_numbers[j]
    
    # Display results
    print('\nOriginal order: ' + ', '.join(map(str, numbers)))
    print('Mean average is: ' + str(Mean))
    print('Ascending order: ' + ', '.join(map(str, sorted_numbers)))
    print('Descending order: ' + ', '.join(map(str, sorted_numbers[::-1])))
    
    playAgain = input("\nDo you want to sort more numbers? Y/N ").lower()
    
    if playAgain not in {"y","n"}:
        print("Please enter a valid option: ")
    elif playAgain == "y":
        main()
    elif playAgain == "n":
        print("Exiting program...")
        exit()

main()