import java.util.*;

class Solution {
    public int[] solution(int[] numbers, String direction) {
        int[] answer = new int[numbers.length];
        
        if (direction.equals("left")){ 
            answer[numbers.length-1]=numbers[0];
            for(int i=1;i<numbers.length;i++){
                answer[i-1]=numbers[i];
            }
        }
        
        else{
            answer[0]=numbers[numbers.length-1];
            for(int i=0;i<numbers.length-1;i++){
                answer[i+1]=numbers[i];
            }
        }
        return answer;
    }
}


//왜 direction == "left"가 안된것...? => 문자열이라!
//문자열이 가지고 있는 값의 비교는 stirng 내장함수를 써야함