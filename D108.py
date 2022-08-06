def isShifted(A, B):
    if A == B:
        return True
    for i in range(len(A)):
        A = shift(A)
        if A == B:
            return True
    return False

def shift(str):
    return str[1:] + str[0]

print(shift('abcde'))
print(isShifted('abcde', 'cdeab'))
print(isShifted('abc', 'acb'))
print(isShifted('eabcd', 'abcde'))