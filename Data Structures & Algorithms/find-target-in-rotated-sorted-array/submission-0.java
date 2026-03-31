class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int middle = left + (right - left) / 2;
            if (nums[middle] == target) {
                return middle;
            }

            if (nums[left] <= nums[middle]) {
                // left half is sorted 
                if (target >= nums[left] && target < nums[middle]) {
                    // target is in the left half 
                    right = middle - 1;
                } else {
                    //target is in the right half
                    left = middle + 1;
                }
            } else {
                // right half is sorted 
                if (target > nums[middle] && target <= nums[right]) {
                    // target is in the right half
                    left = middle + 1;
                } else {
                    // target is in the left half
                    right = middle - 1;
                }
            }
        }
        return -1;
    }
}
