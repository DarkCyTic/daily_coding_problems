def remove_bigger_numbers(k, numbers):
    for num in numbers:
        if num > k:
            numbers.remove(num)

    return numbers


def solve(k, numbers):
    numbers = remove_bigger_numbers(k, numbers)

    result = False

    for num in numbers:
        complement = k - num
        if complement in numbers:
            result = True
            break

    return result


if __name__ == "__main__":
    # Get input
    k = int(input("k: "))
    numbers = input("numbers: ")

    # Split, convert and put in array the numbers
    numbers = list(map(int, numbers.split(' ')))

    result = solve(k, numbers)
    print("Result: ", result)