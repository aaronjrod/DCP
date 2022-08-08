
def fibonacci_memo(n):
    val = [0 for x in range(n+1)]
    return fibonacci_helper(n, val)
    #return val[n]

def fibonacci_helper(i, val):
    if i <= 1:
        return i
    
    if val[i] <= 1:
        val[i] = fibonacci_helper(i-1, val) + fibonacci_helper(i-2, val)
    return val[i]

arr = [0,1,6]
for val in range(7): 
    print(fibonacci_memo(val))
