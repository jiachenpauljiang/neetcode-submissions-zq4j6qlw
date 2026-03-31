class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<String> seen = new HashSet<>();

        for (int r = 0 ; r < 9 ; r++) {
            for (int c = 0 ; c < 9 ; c++) {
                char curNum = board[r][c];

                if (curNum != '.') {
                    int boxRow = r / 3;
                    int boxCol = c / 3;

                    //checks dup in the current row 
                    if (!seen.add(curNum + "inrow" + r)) {
                        return false;
                    }

                    // checks dup in the current col
                    if (!seen.add(curNum + "incol" + c)) {
                        return false;
                    }

                    //checks dup in the current sub box
                    if (!seen.add(curNum + "inboxrow" + boxRow + "col" + boxCol)) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}