class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int left = 0;
        int right = matrix.length * matrix[0].length - 1;

        while (left <= right) {
            // 6 -> (1, 2), matrix.length = 3
            int middle = left + (right - left) / 2;
            int row = middle / matrix[0].length;
            int col = middle % matrix[0].length;
            int elementValue = matrix[row][col];

            if (elementValue == target) {
                return true;
            } else if (elementValue > target) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }

        return false;
    }
}
