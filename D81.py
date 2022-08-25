
def possible_repr(digit_str, mapping):
    repr_list = []
    for digit in digit_str:
        possible_chars = mapping[digit]
        open_list = []

        if not repr_list:
            repr_list += possible_chars
            continue

        for output in repr_list:
            for char in possible_chars:
                open_list.append(output + char)
        repr_list = open_list
    return repr_list
        
mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], }

print(possible_repr("232", mapping))