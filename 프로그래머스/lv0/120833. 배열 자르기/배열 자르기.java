class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        int answer_length = num2-num1+1;
        int[] answer = new int[answer_length];
        int i=0;

        for(int j=num1;j<=num2;j++){
            answer[i] = numbers[j];
            i++;
        }
        return answer;
    }
}