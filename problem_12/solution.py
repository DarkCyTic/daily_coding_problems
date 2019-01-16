def solve(stairs, steps):
    possibilities = 0

    for step in steps:
        if stairs - step > 0:
            possibilities = possibilities + solve(stairs - step, steps)
        if stairs - step == 0:
            possibilities = possibilities + 1

    return possibilities
        

if __name__ == "__main__":
    stairs = int(input("Number of stairs: "))
    raw_numbers = input("Possible steps: ")
    steps = list(map(int, raw_numbers.split(' ')))

    print("Possible ways:", solve(stairs, steps))