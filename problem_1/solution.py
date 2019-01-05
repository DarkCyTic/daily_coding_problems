def remove_bigger_numbers(k, numbers):
    for num in numbers:
        if num > k:
            numbers.remove(num)

    return numbers


def solve(k, numbers):
    # Remove numbers bigger than k
    numbers = remove_bigger_numbers(k, numbers)
    # Sort the list
    numbers.sort()

    # Variables marking the first and last index of the list
    i = 0
    j = len(numbers) - 1

    while i < j:
        sum = numbers[i] + numbers[j]

        if sum < k:
            i += 1
            continue
        else if sum > k
            j += 1
            continue
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