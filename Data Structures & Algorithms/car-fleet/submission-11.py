class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lines = list(zip(speed, position))
        lines.sort(key=lambda x: x[1], reverse=True)
        stack = collections.deque()
        for t, x in lines:
            time = (target - x)/t
            if stack and time <= stack[-1]:
                prev = stack[-1]
                stack.pop()
                stack.append(max(time, prev))
            else:
                stack.append(time)
        return len(stack)

