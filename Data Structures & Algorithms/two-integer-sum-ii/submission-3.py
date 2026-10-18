class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer sol?
        n = len(numbers)
        left = 0
        right = n-1
        while left < right:
            # if target - left > right, left += 1
            # elif target - left < right, right -= 1
            # else return [left, right]
            if target - numbers[left] > numbers[right]:
                left += 1
            elif target - numbers[left] < numbers[right]:
                right -= 1
            else:
                return [left+1, right+1]
        