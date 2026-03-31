class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        int i = 0;
        while (i < nums.length - 2) {
            int j = i + 1;
            while (j < nums.length - 1) {
                int k = j + 1;
                while (k < nums.length) {
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        List<Integer> candidate = new ArrayList<>(List.of(nums[i], nums[j], nums[k]));
                        candidate.sort(null);
                        if (!results.contains(candidate)) {
                            results.add(candidate);
                        }
                    }
                    k++;
                }
                j++;
            }
            i++;
        }

        return results;
    }
}
