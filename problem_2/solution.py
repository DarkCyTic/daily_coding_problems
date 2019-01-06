def solve(integers):
    product = 1
    
    for integer in integers:
        product *= integer

    result = [ int(product / integer) for integer in integers ]
    
    return result


if __name__ == "__main__":
    raw_numbers = input("Array of integers: ")
    integers = list(map(int, raw_numbers.split(' ')))

    result = solve(integers)

    print(result)