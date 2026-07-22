import math
class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        seen = set()
        while num != 1:
            if num in seen:
                return False
            seen.add(num)
            temp = num
            res = 0
            print(num)
            for i in range(int(math.log(num))+1):
                res += (temp % 10) ** 2
                temp //= 10
            num = res
        return True