# /usr/bin/python3
# Page 73 of Cracking the Coding Interview
# 1.3 Given two strings, write a method to decide if one is permutation of the other.

def isPerm(str1,str2):
    if(len(str1) != len(str2)):
        return False
    check1 = dict()
    check2 = dict()
    for i in range(len(str1)):
        if(str1[i] in check1):
            check1[str1[i]]+=1
        else:
            check1[str1[i]] = 1
        if(str2[i] in check2):
            check2[str2[i]]+=1
        else:
            check2[str2[i]] = 1
    return check1 == check2

def isPermNoDS(str1,str2):
    if(len(str1) != len(str2)):
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)
    return str1 == str2


if __name__ == "__main__":
    assert(not isPerm('a',''))
    assert(not isPerm('abab','abbc'))
    assert(isPerm('',''))
    assert(isPerm('ababb','aabbb'))
    assert(isPermNoDS('ababb','aabbb'))
