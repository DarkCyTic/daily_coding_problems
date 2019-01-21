def solve(arr_numbers, k):
    for index, num in enumerate(arr_numbers):
        if index < k - 1:
            continue
        new_array = arr_numbers[index - (k - 1):index + 1]
        max = new_array[0]
        for n in new_array:
            if n > max:
                max = n
        print(max)

if __name__ == "__main__":
    raw_numbers = input("Array of numbers: ")
    arr_numbers = list(map(int, raw_numbers.split(' ')))
    # arr_numbers = [10, 5, 2, 7, 8, 7]

    k = int(input("The number k: "))
    # k = 3   

    solve(arr_numbers, k)