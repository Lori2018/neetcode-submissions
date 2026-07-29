from collections import deque

class MinStack:

    def __init__(self):
        self.min_ = None
        self.stack = deque()

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_ = val
        if val < self.min_: 
            self.stack.append(val - self.min_)
            self.min_ = val
        else:
            self.stack.append(val - self.min_)

    def pop(self) -> None:
        elem = self.stack.pop()
        if elem < 0:
            self.min_ -= elem


    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.min_
        return self.stack[-1] + self.min_

    def getMin(self) -> int:
        return self.min_
