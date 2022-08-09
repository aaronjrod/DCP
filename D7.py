def is_valid(msg, i):
    for j in range(i+1, i+3):
        val = int(msg[i:j])
        if 0 >= val or val > 26:
            return False
    return True

def num_decodings(msg):
    count = 0
    for i in range(len(msg)):
        if is_valid(msg, i):
            count += 1
    return count

def num_decodings(msg):
    return num_decodings_helper(msg, [], [])

def num_decodings_helper(msg, code_list, code):
    if len(msg) == 0:
        code_list.append(code)
        return
    
    count = 0
    for i in range(1, min(3, len(msg)+1)):
        val = int(msg[:i])
        if 0 < val and val <= 26:
            num_decodings_helper(msg[i:], code_list, code+[val])
    return code_list

arr = ['', '123426']
for i in arr:
    print(num_decodings(i))  