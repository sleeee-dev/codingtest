import java.util.Arrays;

class Solution {
    public String solution(String s) {
        String answer = "";        
        String[] arr= s.split("");
        int cnt = 0;
        
        Arrays.sort(arr); //split한 문자열을 사전순으로 정렬
        
        for(int i=0; i<arr.length; i++){
            cnt = 0;
            
            for(int j=0; j<arr.length; j++){
                if(arr[i].equals(arr[j])){
                    cnt++; //같은 문자가 있을때 cnt++
                }                
            }
            if(cnt == 1){ //cnt==1 즉, 같은 문자가 자기자신 하나일때만 answer로 return
                answer += arr[i];
            }
        }
        return answer;
    }
}