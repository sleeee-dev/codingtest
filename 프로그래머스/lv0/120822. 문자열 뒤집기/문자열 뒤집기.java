class Solution {
    public String solution(String my_string) {
        String answer = "";
        String[] str = my_string.split("");
        int len = my_string.length()-1;
        
        for (int i=len;i>=0;i--){
            answer += str[i];
        }
        return answer;
    }
}