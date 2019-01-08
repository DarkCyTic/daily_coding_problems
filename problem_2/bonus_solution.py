def solve(integers):
    result = []
    integers_len = len(integers)

    left_product = 1
    left_products = []

    for integer in integers:
        left_product *= integer
        left_products.append(left_product)

    right_product = 1
    right_products = []

    index = len(integers) - 1

    while index > 0:
        right_product *= integers[index]
        right_products.append(right_product)
        index -= 1

    right_products_len = len(right_products)

    for counter in range(integers_len):
        product = 1
        if counter > 0:
            product *= left_products[counter - 1]
        if counter < len(integers) - 1:
            product *= right_products[right_products_len - (counter + 1)]
        result.append(product)

    return result


if __name__ == "__main__":
    raw_numbers = input("Array of integers: ")
    integers = list(map(int, raw_numbers.split(' ')))

    result = solve(integers)

    print(result)