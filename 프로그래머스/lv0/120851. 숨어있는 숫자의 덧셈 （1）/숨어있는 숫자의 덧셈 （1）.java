class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String str1 = my_string.replaceAll("[a-zA-Z]", ""); //[]"범위만큼 ""공백으로 대체
        String[] str2 = str1.split(""); //쪼개기
        
        for(int i=0 ; i<str2.length; i++){
            answer += Integer.parseInt(str2[i]); //정수로 형변환해서 더하기
        }
        return answer;
    }
}