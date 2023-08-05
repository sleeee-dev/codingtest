class Solution {
    public String solution(String bin1, String bin2) {
        String answer = "";
        answer = Integer.toBinaryString(Integer.parseInt(bin1,2) + Integer.parseInt(bin2,2));
        return answer;
    }
}


//Integer.parseInt(bin1,2);
//2진수 bin1을 10진수로 변환
//Integer.toBinaryString(bin1);
//10진수 bin1을 2진수 형태의 string으로 변환