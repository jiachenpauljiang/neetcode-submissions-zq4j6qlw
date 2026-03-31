class Solution {
    public int findMin(int[] nums) {
        int leftIndex = 0;
        int rightIndex = nums.length - 1;

        while (leftIndex < rightIndex) {
            int middleIndex = (leftIndex + (rightIndex - leftIndex) / 2);

            if (nums[middleIndex] < nums[rightIndex]) {
                // minimum is on the left half
                rightIndex = middleIndex;
            } else {
                // minimum is in the right half 
                leftIndex = middleIndex + 1;
            }
        }
        return nums[leftIndex];
    }
}
