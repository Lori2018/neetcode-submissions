from collections import deque

class MinStack:

    def __init__(self):
        self.min_ = None
        self.stack = deque()
        self.size = 0

    def push(self, val: int) -> None:
        if self.min_ == None:
            self.min_ = val
        if val < self.min_: 
            self.stack.append(val - self.min_)
            self.min_ = val
        else:
            self.stack.append(val - self.min_)
        self.size += 1

    def pop(self) -> None:
        elem = self.stack.pop()
        if elem < 0:
            self.min_ -= elem
        self.size -= 1
        if self.size == 0:
            self.min_ = None


    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.min_
        return self.stack[-1] + self.min_

    def getMin(self) -> int:
        return self.min_
