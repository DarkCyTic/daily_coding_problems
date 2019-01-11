def cons(a, b):
    def pair(f):
        return f(a ,b)
    return pair

def car(pair):
    def first(a ,b):
        return a
    return pair(first)

def cdr(pair):
    def last(a ,b):
        return b
    return pair(last)

if __name__ == "__main__":
    first = car(cons(3, 4))
    last = cdr(cons(3, 4))

    print("First - ", first)
    print("Last - ", last)
    