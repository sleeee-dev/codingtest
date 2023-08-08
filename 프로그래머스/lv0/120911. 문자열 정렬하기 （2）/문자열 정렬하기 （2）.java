import java.util.Arrays;

class Solution {
    public String solution(String my_string) {
        String result = "";

        char[] charArr = my_string.toLowerCase().toCharArray();
        Arrays.sort(charArr);

        result = new String(charArr);
        return result;
    }
}