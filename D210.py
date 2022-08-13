# A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

# if n is even, the next number in the sequence is n / 2
# if n is odd, the next number in the sequence is 3n + 1
# It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

# Bonus: What input n <= 1000000 gives the longest sequence?

def collatz(n, list=[]):
    list.append(n)
    if n <= 1:
        return list

    if n % 2:
        return collatz(3*n+1, list)
    return collatz(int(n/2), list)

optimal_input = 0
for i in range(1000000):
    optimal_input = max(optimal_input, len(collatz(i)))

print(optimal_input)