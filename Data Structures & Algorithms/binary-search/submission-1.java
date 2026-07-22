class Solution {
    public int search(int[] nums, int target) {
        return bs(nums, 0, nums.length, target);
    }

    public int bs(int[] nums, int start, int stop, int target) {
        if (start >= stop) {
            return -1;
        }

        int mid = (stop - start) / 2 + start;
        if (target == nums[mid]) {
            return mid;
        } else if (target < nums[mid]) {
            return bs(nums, 0, mid, target);
        } else {
            return bs(nums, mid + 1, stop, target);
        }
    }
}
