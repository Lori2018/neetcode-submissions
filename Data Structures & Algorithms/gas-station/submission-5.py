class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        cur = 0
        n = len(gas)
        for i in range(n):
            cur += gas[i] - cost[i]
            print(cur)
            if cur < 0:
                cur = 0
                start = i+1
        return start