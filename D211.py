def find_starting(string, pattern):
    count = 0
    for i in range(len(string)):
        for j in range(len(pattern)):
            if i+j >= len(string) or string[i+j] != pattern[j]:
                break
            if j+1 == len(pattern):
                count += 1
    return count

print(find_starting("abracadabra", "abr"))
print(find_starting("abracadabra", "abra"))
print(find_starting("abracadabra", "a"))

print(find_starting("aaaa", "a"))