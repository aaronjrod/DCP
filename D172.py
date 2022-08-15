# Good morning! Here's your coding interview problem for today.

# This problem was asked by Dropbox.

# Given a string s and a list of words words, where each word is the same length, find all starting indices of substrings in s that is a concatenation of every word in words exactly once.

# For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

# Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are no substrings composed of "dog" and "cat" in s.

# The order of the indices does not matter.

def find_concat(s, words):
    out = []
    for i in range(len(s)):
        if find_concat_helper(s[i:], words.copy()):
            out.append(i)
    return out

def find_concat_helper(s, words):
    if not words:
        return True

    for i in words:
        if s[:len(i)] == i:
            words.remove(i)
            return find_concat_helper(s[len(i):], words)
    return False
        
print(find_concat('dogcatcatcodecatdog', ["cat", "dog"]))
print(find_concat('barfoobazbitbyte', ["cat", "dog"]))