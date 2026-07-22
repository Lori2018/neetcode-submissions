class Solution:
    def hammingWeight(self, n: int) -> int:
        arr = [0] * 32

        for i in range(31, 0, -1):
            if n < pow(2, i):
                continue
            elif n == pow(2, i):
                return 1 + Counter(arr)[1]
            arr[i] = 1
            n -= pow(2, i)
        return Counter(arr)[1] + 1 if n != 0 else 0