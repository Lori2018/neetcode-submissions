from collections import defaultdict

class Solution:
    def trap(self, height: List[int]) -> int:
        # store indices of closest biggest on left & biggest on right
        # get minimum & add to volume if min is > cur height
        left = 0
        leftMax = 0
        right = len(height) - 1
        lefts = [0] * len(height)
        rights = [0] * len(height)
        vol = 0

        while left < len(height):
            if left == 0:
                lefts[0] = height[0]
            else:
                lefts[left] = max(height[left - 1], lefts[left - 1])
            left += 1

        while right > 0:
            if right == len(height) - 1:
                rights[len(height) - 1] = height[len(height) - 1]
            else:
                rights[right] = max(height[right + 1], rights[right + 1])
            right -= 1
        # print(lefts)

        left = 0
        while left < len(height):
            print(lefts[left], rights[left])
            add = min(lefts[left], rights[left]) - height[left]
            if add > 0:
                vol += add
            left += 1
        return vol
