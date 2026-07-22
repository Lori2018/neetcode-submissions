class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        max_val = 2 ** 31 - 1
        min_val = -2 ** 31 
        for digit in str(x)[::-1]:
            if digit == "-":
                res *= -1
            else:
                res *= 10
                res += int(digit) 
            if res > max_val or res < min_val:
                return 0
        return res