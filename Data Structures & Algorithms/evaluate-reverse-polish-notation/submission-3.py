class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # if number, push to stack
        # if operation, pop top 2 numbers off stack and push result
        stack = []
        for tok in tokens:
            if tok == '+':
                num1 = stack.pop()
                num2 = stack.pop() 
                stack.append(num1 + num2)
            elif tok == '*':
                num1 = stack.pop()
                num2 = stack.pop() 
                stack.append(num1 * num2)
            elif tok == "-":
                num1 = stack.pop()
                num2 = stack.pop() 
                stack.append(num2 - num1)
            elif tok == "/":
                num1 = stack.pop()
                num2 = stack.pop() 
                stack.append(int(num2 / num1))
            else: 
                stack.append(int(tok))
            print(stack)
        return stack.pop()