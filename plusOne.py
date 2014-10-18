class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        jin = 1
        for i in range(len(digits)):
            if digits[-(i+1)] + jin <= 9:
                digits[-(i+1)] += jin
                jin = 0
                break
            digits[-(i+1)] = 0
        if jin:
            digits.insert(0, 1)
        return digits