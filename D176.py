def one_to_one_char_map(s1, s2):
    char_map = {}
    for i in range(len(s1)):
        if s1[i] in char_map and char_map[s1[i]] != s2[i]:
            return False
        char_map[s1[i]] = s2[i]
    return True

print(one_to_one_char_map('abc','bcd'))
print(one_to_one_char_map('foo','bar'))
print(one_to_one_char_map('foo','baa'))