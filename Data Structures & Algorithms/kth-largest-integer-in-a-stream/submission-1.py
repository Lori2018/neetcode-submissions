import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.length = 0
        self.k = k
        for num in nums:
            if self.length < k:
                heapq.heappush(self.heap, num)
                self.length += 1
            elif num > self.heap[0] and self.length == k:
                heapq.heappushpop(self.heap, num)
                

    def add(self, val: int) -> int:
        if self.length < self.k:
            heapq.heappush(self.heap, val)
            self.length += 1
        elif val > self.heap[0] and self.length == self.k:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
