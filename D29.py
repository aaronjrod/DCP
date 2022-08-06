def encode(string):
    if not string:
        return ""

    temp = ""
    out = ""
    while len(string) > 0:
        if temp == "":
            temp = string[0]
        elif temp[0] == string[0]:
            temp += string[0]
        else:
            out += str(len(temp))
            out += temp[0]
            temp = string[0]
        string = string[1:]
    
    out += str(len(temp))
    out += temp[0]

    return out

def decode(string):
    out = ""
    if not string or len(string) == 0 or not string[0].isnumeric():
        return ""
    while len(string) > 0:
        num = int(string[0])
        for i in range(0,num):
            out += string[1]
        string = string[2:]
    return out


print(encode(""))
print(encode("hi"))
print(encode("AAAABBBCCDAA"))

print(decode(encode("")))
print(decode(encode("hi")))
print(decode(encode("AAAABBBCCDAA")))
print(decode("AAAABBBCCDAA"))

