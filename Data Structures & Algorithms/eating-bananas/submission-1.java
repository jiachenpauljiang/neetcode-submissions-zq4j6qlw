class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        // binary search 
        int left = 1;
        int right = Arrays.stream(piles).max().getAsInt();
        int result = right;

        while (left <= right) {

            int middle = left + (right - left) / 2;
            int totalTime = 0;

            for (int pile : piles) {
                totalTime += Math.ceil((double) pile / middle);
            }

            if (totalTime > h) {
                left = middle + 1;
            } else {
                result = middle;
                right = middle - 1;
            }
        }
        return result;
    }
}
