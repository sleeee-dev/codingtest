class Solution {
    public String solution(String my_string, int num1, int num2) {
        String answer = "";
        String str_n2 = "";
        String[] str = my_string.split("");
        int len = my_string.length()-1;
        str_n2 = str[num2];
        str[num2] = str[num1];
        str[num1] = str_n2;
        
        for (int i = 0; i<=len;i++ ){
            answer += str[i];
        }
        return answer;
    }
}