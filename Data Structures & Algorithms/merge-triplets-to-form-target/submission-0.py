class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # iterate and replace if closer to target and meets reqs
        cur = None
        for triplet in triplets:
            if not cur and triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                cur = triplet
        print(f"cur: {cur}")
        if not cur:
            return False

        for triplet in triplets:
            if cur and triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2] and (triplet[0] > cur[0] or triplet[1] > cur[1] or triplet[2] > cur[2]):
                print(f"maxxing {cur} and {triplet}")
                cur[0] = max(cur[0], triplet[0])
                cur[1] = max(cur[1], triplet[1])
                cur[2] = max(cur[2], triplet[2])
                print(f"cur is now {cur}")
        
        return cur == target