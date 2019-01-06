def solve(integers):
    result = []
    product = 1

    for integer in integers:
        product *= integer

    for integer in integers:
        current_product = int(product / integer)
        result.append(current_product)
    
    return result


if __name__ == "__main__":
    raw_numbers = input("Array of integers: ")
    integers = list(map(int, raw_numbers.split(' ')))

    result = solve(integers)

    print(result)