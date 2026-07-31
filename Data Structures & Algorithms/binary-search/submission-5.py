class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search_(i, j):
            mid = (j+i)//2
            print(nums[i:j+1])
            print(i, j)
            if j == i:
                return i if target == nums[j] else -1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return search_(mid+1, j)
            else:
                return search_(i, mid)
        return search_(0, len(nums)-1)