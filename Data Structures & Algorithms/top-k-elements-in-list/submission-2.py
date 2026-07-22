class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash map of counters
        m = {}
        for num in nums: 
            if num in m: 
                m[num] += 1
            else: 
                m[num] = 1
        # new dict where key is count & value is list of numbers
        x = {}
        for entry in m: 
            if m[entry] in x:
                x[m[entry]] += [entry]
            else: 
                x[m[entry]] = [entry]
        
        # sort list of keys 
        l = list(x.keys())
        l.sort()
        l.reverse()

        # get top k in list, return numbers 
        i1 = 0 # count
        j = 0 # item with that count
        sol = []
        for i in range(k):
            count = l[i1]
            sol += [x[count][j]]
            if j == len(x[count]) - 1:
                i1 += 1
                j = 0
            else:
                j += 1
        
        return sol
