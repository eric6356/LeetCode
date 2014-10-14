def isPalindrome(s):
    s = s.lower()
    t = list()
    for i in s:
        if ord('a') <= ord(i) <= ord('z') or ord('0') <= ord(i) <= ord('9'):
            t.append(i)
    n = len(t)
    print t
    return t[:n/2] == t[:(n-1)/2:-1]
print isPalindrome("1a2")