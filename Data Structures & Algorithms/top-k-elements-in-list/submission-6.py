import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap of size k
        # get counts of each number and keep in list of tuples 
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        print(counts)
        h = []
        for item in counts:
            if len(h) == k:
                if h[0][0] < counts[item]:
                    heapq.heappop(h)
                    heapq.heappush(h, (counts[item], item))
            else:
                heapq.heappush(h, (counts[item], item))

        return [item[1] for item in h]