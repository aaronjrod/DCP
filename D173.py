def flatten_dict(dict):
    return flatten_dict_helper(dict, {}, "")

def flatten_dict_helper(in_dict, out_dict, prefix):
    for item in in_dict.keys():
        new_key = prefix+item
        if type(in_dict[item]) is dict:
            flatten_dict_helper(in_dict[item], out_dict, new_key+'.')
        else:
            out_dict[new_key] = in_dict[item]
    return out_dict

in_dict = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
print(flatten_dict(in_dict))