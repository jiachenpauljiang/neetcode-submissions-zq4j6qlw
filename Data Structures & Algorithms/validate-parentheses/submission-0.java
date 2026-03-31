class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (Character curChar : s.toCharArray()) {
            if (curChar == '(' || curChar == '[' || curChar == '{') {
                stack.push(curChar);
            } else {
                // it's a closing bracket 
                if (stack.isEmpty()) {
                    // this means the closing bracket is the first, so return false 
                    return false;
                }

                if (curChar == '}' && stack.pop() != '{' 
                    || curChar == ']' && stack.pop() != '['
                    || curChar == ')' && stack.pop() != '(') {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}
