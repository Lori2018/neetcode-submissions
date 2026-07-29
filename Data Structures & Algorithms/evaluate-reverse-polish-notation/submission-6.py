class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()
        for tok in tokens:
            match tok:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(y - x)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(int(y / x))
                case _:
                    stack.append(int(tok))
            print(stack)
        return stack[-1]