# /usr/bin/python3
# Page 73 of Cracking the Coding Interview
# 1.4 * Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end of the string to hold the additional characters, and that you are given the "true" length of the string. (Note: if implementing in Java, please use a character array so you can perform this operation in place.)
#
# EXAMPLE
# Input : "Mr John Smith    "
# Output: "Mr%20John%20Smith"

def replaceSpace(inp):
    inp = inp.strip()
    for i in range(len(inp)):
        if inp[i] == ' ':
            inp = inp[:i] + '%20' + inp[i+1:]
    return inp


if __name__ == "__main__":
    assert(replaceSpace('') == '')
    assert(replaceSpace('asd f')== 'asd%20f')
