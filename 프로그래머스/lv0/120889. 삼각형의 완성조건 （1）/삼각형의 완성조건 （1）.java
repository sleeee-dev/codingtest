class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        int maxside = 0;
        int sumsides = 0;
        
        if(sides[0]>sides[1] && sides[0]>sides[2]){
            maxside = sides[0];
        }
        else if(sides[1]>sides[0] && sides[1]>sides[2]){
            maxside = sides[1];
        }
        else if(sides[2]>sides[0] && sides[2]>sides[1]){
            maxside = sides[2];
        }else{
            answer = 2;
        }
        
        for(int i=0;i<sides.length;i++){
            if(sides[i]!=maxside){
                sumsides +=sides[i];
            }
        }
        
        if(maxside<sumsides){
            answer = 1;
        }
        else{
            answer = 2;
        }
        
        return answer;
    }
}


/*
//정렬 sort() 쓰면 빠르게 해결된다 ㅠ.
import java.util.Arrays;

class Solution {
    public int solution(int[] sides) {
        Arrays.sort(sides);
        return sides[0] + sides[1] > sides[2] ? 1 : 2;
    }
}
*/