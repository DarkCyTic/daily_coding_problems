def solve(k, numbers):
    result = False

    for num in numbers:
        numbers.remove(num)

        for number in numbers:
            if(number == k - num):
                numbers.remove(number)
                result = True
                break

        if result:
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