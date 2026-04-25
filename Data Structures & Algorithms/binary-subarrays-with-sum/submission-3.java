class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            int curSum = 0;
            for (int j = i; j < nums.length; j++) {
                curSum += nums[j];
                if (curSum == goal) {
                    res += 1;
                    continue;
                }
            }
        }
        return res;
    }
}