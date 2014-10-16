class Solution:
    # @return a boolean
    def isValid(self, s):
        stk = list()
        for c in s:
            if c == '(' or c == '[' or c == '}':
                stk.append(c)
            if c == ')':
                if not stk or stk.pop() != '(':
                    return False
            if c == ']':
                if not stk or stk.pop() != '[':
                    return False
            if c == '}':
                if not stk or stk.pop() != '}':
                    return False
        if stk:
            return False
        return True
