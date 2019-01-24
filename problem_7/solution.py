def create_fib_array(n):
    fib_array = [1, 1]
    
    for i in range(n - 1):
        fib_array.append(fib_array[i] + fib_array[i + 1])

    return fib_array

def solve(num_array):
    num_len = len(num_array)
    fib_array = create_fib_array(num_len)

    cur_len = 0
    pairs = 1

    for index, n in enumerate(num_array):
        cur_len += 1
        if index == num_len - 1:
            pairs *= fib_array[cur_len]
        elif (n == 2 and num_array[index + 1] > 6) or n > 2:
            pairs *= fib_array[cur_len]
            cur_len = 0

    return pairs

if __name__ == "__main__":
    # num_array = [2, 2, 7, 2, 8]
    raw_numbers = input("Your message: ")
    num_array = list(map(int, list(raw_numbers)))
    print(num_array)
    pairs = solve(num_array)

    print("Result is:", pairs)