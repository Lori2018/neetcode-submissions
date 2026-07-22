class MinStack:
    def __init__(self):
        self.stack = []
        self.minNum = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1:
            self.minNum = 0
        elif val < self.stack[self.minNum]:
            self.minNum = len(self.stack) - 1


    def pop(self) -> None:
        minNumI = self.stack[self.minNum]
        num = self.stack.pop()
        if minNumI == num:
            i = 0
            self.minNum = 0
            for i in range(len(self.stack)):
                if self.stack[self.minNum] > self.stack[i]:
                    self.minNum = i

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.stack[self.minNum]
