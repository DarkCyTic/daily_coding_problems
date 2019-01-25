def solve(num_array):
    sum = 0

    index = 0 
    while len(num_array) > 0:
        # print(index, num_array, sum)
        n = num_array[index]
        if index == 0:
            if len(num_array) == 1:
                if sum + n > sum or sum == 0:
                    sum += n
                    break
                else:
                    break
            elif n >= num_array[index + 1]:
                del num_array[index + 1]
                del num_array[index]
                if sum + n > sum or sum == 0:
                    sum += n
            else:
                index += 1
        elif index == len(num_array) - 1:
            if n >= num_array[index - 1]:
                del num_array[index]
                del num_array[index - 1]
                index = len(num_array) - 1
                if sum + n > sum or sum == 0:
                    sum += n
            else:
                index -= 1

        else:
            if n >= num_array[index - 1] and n >= num_array[index + 1]:
                del num_array[index + 1]
                del num_array[index - 1]
                index -= 1
                if sum + n > sum:
                    num_array[index] = float("-inf")
                    sum += n
            else:
                index += 1
    return sum

if __name__ == '__main__':
    test_cases = [
        [[5, 1, 1, 5], 10],
        [[-5, -5, -5], -5],
        [[-5, -5, -5, -5], -5],
        [[2, 4, 6, 2, 5], 13],
        [[-5, -1, -1, -5], -1],
        [[2, 4, 6, 8, 9, 10], 22],
        [[2, 4, 6, 2, 5, 7, 3, 9], 24],
        [[8, -1, 3, 0, 4, 5, 7], 22],
        [[-1, 7, 3, 2, 5, 1], 12],
        [[1, 2, 3, 4, 5], 9],
        [[5, 4, 3, 2, 1], 9],
        [[0], 0],
        [[-1], -1]
    ]

    for case in test_cases:
        test_case = case[0]
        case_old = test_case.copy()
        result = solve(test_case)
        assert result == case[1]
        print("{case} = {result}".format(case=case_old, result=result))