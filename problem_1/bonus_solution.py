def solve(k, numbers):
    # Sort the list
    numbers.sort()

    # Variables marking the first and last index of the list
    i = 0
    j = len(numbers) - 1

    while i < j:
        sum = numbers[i] + numbers[j]

        if sum < k:
            i += 1
        elif sum > k:
            j -= 1
        else:
            return True
    
    return False


if __name__ == "__main__":
    # Get input
    k = int(input("k: "))
    numbers = input("numbers: ")

    # Split, convert and put in array the numbers
    numbers = list(map(int, numbers.split(' ')))

    result = solve(k, numbers)
    print("Result: ", result)