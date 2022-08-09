def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def left(a, b):
        return a
    return pair(left)

def cdr(pair):
    def right(a, b):
        return b
    return pair(right)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))

# Explanation: the pair function takes in an input function, f
# To get the value of a, define a function that returns a, given a,b as inputs
# Call pair on this defined function