# /usr/bin/python3
# Page 73 of Cracking the Coding Interview
# 1.1 Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def checkStr(inp):
    try:
        inp = str(inp)
        return inp 
    except TypeError:
        return None


def allUniqueWithDS(inp):
    if (type(inp) != str):
        inp = checkStr(inp)
        if (inp == None):
            return False
    if (len(inp) <= 1):
        return True
    else:
        s = set()
        for c in inp:
            if (c in s):
                return False
            s.add(c)
        return len(s) == len(inp)

def allUniqueWithoutDS(inp):
    if (type(inp) != str):
        inp = checkStr(inp)
        if (inp == None):
            return False
    if (len(inp) <= 1):
        return True
    else:
        temp = sorted(inp)
        for i in range(len(temp)):
            if (i != len(temp) - 1):
                if (temp[i] == temp[i+1]):
                    return False
        return True

if __name__ == '__main__':
    temp = {1,2,3}
    print(allUniqueWithDS(''))
    print(allUniqueWithDS(temp))
    print(allUniqueWithDS('a'))
    print(allUniqueWithDS('aa'))
    print(allUniqueWithDS('ab'))
    print(allUniqueWithoutDS(''))
    print(allUniqueWithoutDS(temp))
    print(allUniqueWithoutDS('a'))
    print(allUniqueWithoutDS('aa'))
    print(allUniqueWithoutDS('ab'))
