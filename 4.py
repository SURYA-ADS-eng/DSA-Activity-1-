"""
4)Valid Anagram (242)
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
"""


s = "anagram"

t = "nagaram"

if( sorted(s) ==  sorted(t)):
    print(True)

else:
    print(False)


#interview level or coding level program

s = "car"

t = "rat"

if(len(s) != len(t)):
    print(false)

else:
    count = {}

    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    for ch in t:
        if ch not in count:
            print(False)
            break
        
        count[ch] -= 1

        if count[ch] < 0:
            print(False)
            break
    else:
        print(True)



        


        



