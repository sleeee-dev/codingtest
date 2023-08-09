class Solution {
    public int solution(String s) {
        String[] sArr = s.split(" "); //공백 기준으로 split
        int answer = 0; 
        
        for(int i=0; i<sArr.length; i++){
            if(sArr[i].equals("Z")){ //Z가 나오면 이전 index값을 뺀다
                answer -= Integer.parseInt(sArr[i-1]);
            }else {
                answer += Integer.parseInt(sArr[i]); //아니라면 해당 index값을 더한다
            }
        }

        return answer;
    }
}