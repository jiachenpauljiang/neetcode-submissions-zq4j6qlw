class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;

        Set<Integer> numSet = new HashSet<>();
        for (int curNum : nums) {
            numSet.add(curNum);
        }

        int longestStreak = 0;
        for (int curNum : numSet) {
            if (!numSet.contains(curNum - 1)) {
                int currentStart = curNum;
                int currentStreak = 1;

                while (numSet.contains(currentStart + 1)) {
                    currentStart += 1;
                    currentStreak += 1;
                }

                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }
        return longestStreak;
    }
}
