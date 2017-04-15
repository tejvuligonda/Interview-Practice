#!/usr/bin/python3
# Page 73 of Cracking the Coding Interview, 5th Ed.
# 1.8 Assume you have a method isSubstring which checks if one word is a substring of another Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (i e , “waterbottle” is a rotation of “erbottlewat”)

def isSubstring(sub,word):
    return sub in word

def isRotation(word,rotation):
    if (len(word) != len(rotation)):
        return False
    wordTwice = (rotation+rotation)
    return isSubstring(word,wordTwice)

if __name__ == '__main__':
    inp1 = ('waterbottle','erbottlewat') 
    inp2 = ('water','erbottlewat') 
    inp3 = ('','')
    inputs = [inp1,inp2,inp3]
    for i in inputs:
        print('input:', i)
        print('output:', isRotation(i[0],i[1]))   
