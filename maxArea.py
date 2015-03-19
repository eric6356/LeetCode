class Solution:
    # @return an integer
    def maxArea(self, height):
        low = 0
        high = len(height)-1
        maxArea = 0
        while high > low:
            maxArea = max(maxArea, min(height[low], height[high]) * (high - low))
            if height[low] > height[high]:
                high -= 1
            else:
                low += 1
        return maxArea
