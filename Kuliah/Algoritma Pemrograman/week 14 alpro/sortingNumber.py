def bubble_sort(arr):
    """
    Sorts a list of numbers in ascending order using the bubble sort algorithm.
    Bubble sort works by repeatedly comparing adjacent elements and swapping them
    if they are in the wrong order. After each full pass through the list, the
    largest unsorted element "bubbles up" to its correct position at the end.
    """
    n = len(arr)
    # Outer loop runs for each element in the list
    for i in range(n):
        # Optimization: track if any swaps happened in this pass
        swapped = False
        # Inner loop compares adjacent elements, but we don't need to check
        # the last i elements since they're already sorted[1][2]
        for j in range(0, n - i - 1):
            # Compare current element with the next one
            if arr[j] > arr[j + 1]:
                # Swap them if they're in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps happened in this pass, the list is already sorted
        # This optimization prevents unnecessary passes[1][2]
        if not swapped:
            break
    return arr

def calculate_mean(numbers):
    """
    Calculates the average (mean) of a list of numbers.
    The mean is found by adding all numbers together and dividing by the count.
    """
    total = sum(numbers)
    count = len(numbers)
    return total / count

def main():
    # Welcome message explaining what the program does
    print('Please enter 10 different numbers below...')
    
    # Create an empty list to store the numbers
    numbers = []
    
    # Loop 10 times to get user input (range(10) gives 0-9, so we use i+1 for counting)
    for i in range(10):
        # Get input, convert to integer, and add to our list
        num = int(input(f'Number {i+1}: '))
        numbers.append(num)
    
    # Calculate the average of all numbers
    mean_value = calculate_mean(numbers)
    
    # Make a copy of the original list to sort (so we keep the original order)
    sorted_numbers = numbers.copy()
    
    # Sort the copied list using our bubble sort function
    sorted_numbers = bubble_sort(sorted_numbers)
    
    # Display results in a clear format
    print('\nOriginal order:', ', '.join(map(str, numbers)))
    print('Mean average is:', mean_value)
    print('Ascending order:', ', '.join(map(str, sorted_numbers)))
    print('Descending order:', ', '.join(map(str, sorted_numbers[::-1])))
    
    # Ask if user wants to run again with clear instructions
    while True:
        play_again = input("\nDo you want to sort more numbers? (Y/N): ").lower()
        if play_again == "y":
            main()  # Restart the program
            return  # Exit current instance after restarting
        elif play_again == "n":
            print("Exiting program...")
            return  # Exit the program
        else:
            print("Please enter Y for yes or N for no.")

# Start the program by calling main()
main()