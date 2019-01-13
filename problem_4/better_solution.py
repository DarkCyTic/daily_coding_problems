def remove_negative_and_zero(num_array):
    """
    Removes all negative numbers and zeros 
    in the given num_array.
    """

    array = []
    for num in num_array:
        if num > 0:
            array.append(num)

    return array


def solve(num_array):
    """
    Function which solves the problem.
    """

    # Remove negative numbers and zeros from the array
    num_array = remove_negative_and_zero(num_array)

    # Iterate array and if the condition is true 
    # change the value at index = value - 1 to negative
    for value in num_array:
        value = abs(value)
        if value <= len(num_array):
            num_array[value - 1] = num_array[value - 1] * (-1)

    # Iterate array and return index + 1 for 
    # the first value that's positive
    for index, value in enumerate(num_array):
        if value > 0:
            return index + 1

    # If no such value is found
    # then the result is the length
    # of the array + 1
    return len(num_array) + 1



if __name__ == "__main__":
    raw_numbers = input("Numbers array: ")
    num_array = list(map(int, raw_numbers.split(' ')))

    result = solve(num_array)

    print("Smallest missing integer: ", result)