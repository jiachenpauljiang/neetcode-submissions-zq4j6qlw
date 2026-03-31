class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            int curProduct = 1;
            int j  = 0;
            while (j < nums.length) {
                if (j != i) {
                    curProduct = curProduct * nums[j];
                }
                j++;
            }
            res[i] = curProduct;
        }
        return res;
    }
}  
