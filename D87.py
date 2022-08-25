def validate_rules(rules):
    KB = set()
    translator = {"N":0, "S":3, "W": 2, "E":1}
    for rule in rules:
        arr = str.split(rule, ' ')
        dir_list = list(arr[1])
        ind_list = [0, 2]
        for dir in dir_list:
            kn1 = (arr[0], arr[2], translator[dir])
            kn1_opp = (arr[0], arr[2], 3-translator[dir])
            kn2 = (arr[2], arr[0], 3-translator[dir])
            kn2_opp = (arr[2], arr[0], translator[dir])
            if kn1_opp in KB or kn2_opp in KB:
                return False
            KB.add(kn1)
            KB.add(kn2)
    return True

print(validate_rules(["A N B", "B NE C", "C N A"]))