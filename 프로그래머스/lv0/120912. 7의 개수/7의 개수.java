import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        String str = Arrays.toString(array); //array를 문자열로 변환 후 split로 쪼개기
        String[] arr = str.split("");
        
        for(int i=0; i<arr.length; i++){
            if(arr[i].equals("7")){ //7이 존재하면 answer++ for문으로 반복 후 리턴
                answer++;
            }
        }
        
        return answer;
    }
}