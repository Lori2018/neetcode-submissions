from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count freq of elems
        # map freq -> elem
        # from k -> 1: get first k 
        n = len(nums)
        freq = [[] for _ in range(n+1)]
        freqMap = defaultdict(int) # elem -> freq
        for i in range(n):
            freqMap[nums[i]] += 1
        for key, v in freqMap.items():
            freq[v].append(key)
        
        sol = []
        count = 0
        print(freq)
        for i in range(n, -1, -1):
            if count < k and len(freq[i]) > 0:
                count += len(freq[i])
                sol.extend(freq[i])
        return sol