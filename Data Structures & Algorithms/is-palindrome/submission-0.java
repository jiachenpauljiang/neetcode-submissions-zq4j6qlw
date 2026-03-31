class Solution {
    public boolean isPalindrome(String s) {
        String cleanString = s.toLowerCase().replaceAll("[^a-z0-9]", "");

        int startIndex = 0;
        int endIndex = cleanString.length() - 1;

        while (startIndex <= endIndex) {
            if (cleanString.charAt(startIndex) != cleanString.charAt(endIndex)) {
                return false;
            }
            startIndex++;
            endIndex--;
        }

        return true;
    }
}
