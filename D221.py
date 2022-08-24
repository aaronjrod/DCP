# EITHER
# Compute a power of 7 --> 7^[0...n]
# Or, sum_ k=0 ^n (7^k)
# q=Want to arrange these in order

def sevenish(n):
    last_power_index = 0
    add_index = 0
    mem = [1] * n

    for i in range(1, n):
        if add_index == last_power_index:
            add_index = 0
            mem[i] = mem[last_power_index] * 7
            last_power_index = i
        else:
            mem[i] = mem[last_power_index] + mem[add_index]
            add_index += 1

    return mem

print(sevenish(15))
