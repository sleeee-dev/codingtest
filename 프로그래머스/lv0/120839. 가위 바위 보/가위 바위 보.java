class Solution {
    public String solution(String rsp) {
        String answer = "";
        String[] str = rsp.split("");
        for (int i=0;i<str.length;i++){
            if(str[i].equals("2")){
                answer += "0";
            }else if(str[i].equals("0")){
                answer += "5";
            }else{
                answer += "2";
            }
        }
    return answer;
    }
}