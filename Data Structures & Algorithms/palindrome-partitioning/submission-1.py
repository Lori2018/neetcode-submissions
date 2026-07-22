class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # do recursion
        # returns all diff ways to partition s
        def part(s):
            if len(s) == 1:
                return [[s]]
            res = []
            for i in range(1, len(s)):
                temp = part(s[i:])
                for t in temp:
                    add = [s[:i]] + t
                    doAdd = True
                    for a in add:
                        if not palindrome(a):
                            doAdd = False
                    if doAdd:
                        res.append(add)
            if palindrome(s):
                res.append([s])
            return res
        def palindrome(x):
            n = len(x)
            for i in range(len(x)//2):
                print(i)
                if x[i] != x[n-i-1]:
                    return False
            return True
        return part(s)
            