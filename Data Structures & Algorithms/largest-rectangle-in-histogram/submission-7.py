class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # build stack
        return max(self.helper(heights), self.helper(heights[::-1]))
    def helper(self, heights):
        print("HELPER")
        stack = []
        area = 0
        for i in range(len(heights) - 1):
            area = max(heights[i], area)
            if heights[i] <= heights[i+1]:# and heights[i] <= heights[i-1]:
                stack.append(i)
        area = max(area, heights[len(heights) - 1])
        stack.append(len(heights) - 1)
        print(stack)
        right = len(heights) - 1
        # if len(stack) > 0 and heights[stack[-1]] > heights[right]:
        #     # iterate backwards through array 
        #     for i in range(len(heights) - 1, 0): 
        #         if heights[i] >= heights[stack[-1]]:
        #             right = i
        #             break
        print("set right to " + str(right))
        while len(stack) > 0:
            i = stack.pop()
            print("processing " + str(i))
            if len(stack) == 0:
                left = 0
            else: 
                temp = []
                while len(stack) > 0:
                    j = stack.pop() 
                    if heights[j] < heights[i]:
                        print(j)
                        left = j + 1 
                        temp.append(j)
                        break
                    elif len(stack) == 0:
                        left = 0
                    temp.append(j)
                print("left: " + str(left))
                print("len: " + str(len(stack)))
                while len(temp) > 0:
                    stack.append(temp.pop())
                print(stack)
                # left = stack[-1] + 1
            area = max(area, heights[i] * (right - left + 1))
            print("rectangle from " + str(left) + " to " + str(right) + " has area " + str(heights[i] * (right - left + 1)))
            while len(stack) > 0 and heights[stack[-1]]  > heights[i]: 
                right = i - 1
                i -= 1
        return area