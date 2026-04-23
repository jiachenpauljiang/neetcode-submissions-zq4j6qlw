class Solution {
    public boolean canJump(int[] nums) {
        if (nums.length == 0 || nums == null) {
            return false;
        }

        int goal = nums.length - 1;

        for (int i = nums.length - 2; i >= 0; i--) {
            if (i + nums[i] >= goal) {
                goal = i;
            }
        }
        return goal == 0;
    }
}
