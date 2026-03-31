class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        if (nums.length == 1) {
            return nums[0];
        }

        int prev_2 = nums[0];
        int prev_1 = Math.max(nums[1], nums[0]);

        for (int i = 2; i < nums.length; i++) {
            int current = Math.max(nums[i] + prev_2, prev_1);
            prev_2 = prev_1;
            prev_1 = current;
        }

        return prev_1;
    }
}