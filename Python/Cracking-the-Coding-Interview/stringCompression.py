#!/usr/bin/python3
# Page 73 of Cracking the Coding Interview
# 1.5 Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. 

def stringCompress(inp):
    count = 0
    result = ''
    for i in range(len(inp)):
        count += 1
        if (i == len(inp) - 1):
            result = result + inp[i] + str(count)
        elif (inp[i] != inp[i+1]):
            result += inp[i]
            result += str(count)
            count = 0
    if (len(result) >= len(inp)):
        return inp
    else:
        return result

if __name__ == '__main__':
    assert(stringCompress('') == '')
    assert(stringCompress('a') == 'a')
    assert(stringCompress('aa') == 'aa')
    assert(stringCompress('abc') == 'abc')
    assert(stringCompress('aaabbcc') == 'a3b2c2')
    
