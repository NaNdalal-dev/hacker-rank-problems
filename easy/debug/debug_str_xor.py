'''
XOR Strings:
https://www.hackerrank.com/challenges/strings-xor/problem
'''
'''
Given:
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] = t[i]:
            res = '0';
        else:
            res = '1';

    return res

s = input()
t = input()
print(strings_xor(s, t))

'''
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res

s = input()
t = input()
print(strings_xor(s, t))
