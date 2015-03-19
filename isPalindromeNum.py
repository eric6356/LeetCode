def isPalindrome(x):
    if x < 0:
        return False
    old_x = x
    new_x = 0
    while x:
        new_x = new_x*10 + x%10
        x /= 10
    return new_x == old_x
print isPalindrome(12321)