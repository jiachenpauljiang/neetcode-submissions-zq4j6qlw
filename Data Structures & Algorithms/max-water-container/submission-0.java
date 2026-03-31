class Solution {
    public int maxArea(int[] heights) {
        int globalMax = 0;
        int i = 0;
        while (i < heights.length - 1) {
            
            int j = i + 1;
            while (j < heights.length) {
                System.out.println("(i, j): " + i + ", " + j);
                int curArea = (j - i) * Math.min(heights[i], heights[j]);
                System.out.println("curArea: " + curArea);
                globalMax = Math.max(curArea, globalMax);
                System.out.println("globalMax: " + globalMax);
                j++;
            }
            i++;
        }
        return globalMax;
    }
}
