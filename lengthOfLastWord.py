def lengthOfLastWord(s):
    if not s:
        return 0
    ss = s.split()
    return len(ss[-1])