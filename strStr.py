class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        i = j = 0
        while i <= len(haystack)-len(needle) and j < len(needle):
            if haystack[i+j] == needle[j]:
                j += 1
            else:
                i += 1
                j = 0
        if j == len(needle):
            return haystack[i:]
        return None