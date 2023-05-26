class Solution {
    public String solution(int age) {
        String answer = "";
        
        String[] ageArr = String.valueOf(age).split("");
        
        for(int i=0; i<ageArr.length; i++){
            answer += (char)(Integer.parseInt(ageArr[i]) + 97); // 아스키코드 97 = a 
        }
        return answer;
    }
}