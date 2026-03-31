class Solution {

    public String encode(List<String> strs) {
        StringBuilder stringBuilder = new StringBuilder();
        for (String s : strs) {
            stringBuilder.append(s.length()).append('#').append(s);
        }
        return stringBuilder.toString();
    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            int delimiter = str.indexOf('#', i);
            int length = Integer.parseInt(str.substring(i, delimiter));
            String curWord = str.substring(delimiter + 1, delimiter + 1 + length);
            result.add(curWord);
            i = delimiter + 1 + length;
        }
        return result;
    }
}
