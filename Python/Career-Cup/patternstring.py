# Given a pattern and a string - find if the string follows the same pattern
# Eg: Pattern : [a b b a], String : cat dog dog cat
# Link: https://careercup.com/question?id=5684019468435456

# Assumptions:
# - Pattern is a list of strings
# - String is a string separated by spaces
# - Each new letter in the pattern is considered a unique string


def main(pattern,string):
    hashmap = {}
    list_string = string.split(" ")
    if len(pattern) != len(list_string):
        return False
    for i in range(len(pattern)):
        p = pattern[i]
        s = list_string[i]
        if p in hashmap.keys():
            if s != hashmap[p]:
                return False
        else:
            if s in hashmap.values():
                return False
            hashmap[p] = s
    return True
        


if __name__ == "__main__":
    print(main(['a','b','c','a'],'cat dog dog cat'))# False
    print(main(['z','z','z','z,','z'],'cat'))       # False

