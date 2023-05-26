import java.util.Arrays;
class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        Arrays.sort(numbers); // 내림차순 정렬. 이 때 맨 뒤에 있는 숫자 2개의 곱이 가장 큰수
        int n1 = numbers[numbers.length-1]*numbers[numbers.length-2];
        int n2 = numbers[0]*numbers[1]; // 맨 앞의 2개의 곱
        // 음수가 2개이상 있을때는 맨 앞의 2개의 곱과도 비교해줘야함
        if(n1>n2){
            answer = n1;
        }else{
            answer = n2;
        }
        return answer;
    }
}