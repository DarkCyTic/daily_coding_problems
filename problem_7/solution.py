def create_fib_array(n):
    fib_array = [1, 1]
    
    for i in range(n):
        fib_array.append(fib_array[i] + fib_array[i + 1])

    return fib_array

def solve(num_array):
    fib_array = create_fib_array(len(num_array))

if __name__ == "__main__":
    num_array = [1, 1, 1, 1, 1]
    solve(num_array)