class MinStack:
    # each number stores numbers below it
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.minStack) == 0:
            self.minStack.append(val)
        elif self.minStack[len(self.minStack) - 1] >= val:
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        num = self.stack.pop()
        if len(self.minStack) > 0 and num == self.minStack[len(self.minStack) - 1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        if len(self.minStack) > 0:
            return self.minStack[len(self.minStack) - 1]
        else:
            return self.stack[len(self.stack) - 1]
