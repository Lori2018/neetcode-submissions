class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # can sort for free
        vals = sorted(Counter(hand))
        counter = Counter(hand)
        print(counter)
        while counter:
            if len(vals) == 0:
                return False
            minVal = vals[0]
            for i in range(groupSize):
                print(minVal+i)
                if counter[minVal+i] == 1:
                    del counter[minVal+i]
                    vals.remove(minVal+i)
                else:
                    counter[minVal+i] -= 1

        return True