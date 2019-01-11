def solve(num_array):
    num_dict = {}

    for num in num_array:
        num_dict[num] = "0"

    biggest_value = 0
    
    for num in num_array:
        if num > biggest_value:
            biggest_value = num

    for i in range(1, biggest_value + 2):
        if not num_dict.__contains__(i):
            return i


if __name__ == "__main__":
    raw_numbers = input('Integer array: ')
    num_array = list(map(int, raw_numbers.split(' ')))
    result = solve(num_array)
    print(result)