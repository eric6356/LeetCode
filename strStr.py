class Solution:
    def next(self, s):
        _j = 0
        _k = -1
        nxt = [-1] * len(s)
        while _j < len(s)-1:
            if _k == -1 or s[_j] == s[_k]:
                _j += 1
                _k += 1
                nxt[_j] = _k
            else:
                _k = nxt[_k]
        return nxt
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        nxt = self.next(needle)
        i = j = 0
        while i <= len(haystack)-1 and j < len(needle):
            if haystack[i] == needle[j]:
                j += 1
                i += 1
            elif nxt[j] == -1:
                j = 0
                i += 1
            else:
                j = nxt[j]
        if j == len(needle):
            return haystack[i-len(needle):]
        return None