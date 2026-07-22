class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights) - 1
        left = 0
        width = len(heights) - 1
        area = min(heights[right], heights[left]) * width
        
        while right != left:
            if heights[left] < heights[right]:
                left += 1
            else: 
                right -= 1
            width -= 1
            area = max(area, min(heights[right], heights[left]) * width)
        return area