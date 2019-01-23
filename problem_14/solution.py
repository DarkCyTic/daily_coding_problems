import random

if __name__ == "__main__":
    in_circle = 0
    out_circle = 0
    dots = int(input("Number of random dots: "))
    for n in range(dots):
        x = random.random()
        y = random.random()
        d = x**2 + y**2
        if d <= 1:
            in_circle = in_circle + 1
        else:
            out_circle = out_circle + 1
    
    pi = (in_circle / dots) * 4
    pi = round(pi, 3)
    print("Pi:", pi)

