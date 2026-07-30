class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack contains items' indices which haven't found their next max
        stack = collections.deque()
        n = len(temperatures)
        res = [0 for _ in range(n)]
        n = len(temperatures)
        for i in range(n):
            if not stack:
                stack.append(i)
            # pop from back
            while stack and temperatures[stack[-1]] < temperatures[i]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res