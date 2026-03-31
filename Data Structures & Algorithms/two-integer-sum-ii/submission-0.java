class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - left - 1;

        while (left < right) {
            int curSum = numbers[left] + numbers[right];

            // if they the sum equals to target, return 
            if (curSum == target) {
                return new int[]{left + 1, right + 1};
            } else if (curSum < target) {
                left++;
            } else {
                right--;
            }
        }
        return new int[]{-1, -1};
    }
}

/**
Max iterations 
[1,2,3,4,5] len = 5

0, len - 0 - 1
1, len - 1 - 1
**/