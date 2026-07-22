class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            if len(stack) != 0:
                if temperatures[stack[-1]] > temperatures[i]:
                    sol[i] = stack[-1] - i
            if len(stack) == 0 or temperatures[stack[-1]] > temperatures[i]:                  
                stack.append(i)
            elif temperatures[stack[-1]] <= temperatures[i]:
                while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[i]:
                    num = stack.pop()
                if len(stack) > 0:
                    sol[i] = stack[-1] - i
                stack.append(i)
            print(stack)
        return sol