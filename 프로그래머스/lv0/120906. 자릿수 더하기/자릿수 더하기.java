class Solution {
    public int solution(int n) {
        int answer = 0;
        while(n>0){
            answer += n%10; //1234%10=4   //123%10=3  //12%10=2 //1%10=1
            n = n/10;       //1234/10=123 //123/10=12 //12/10=1 //1/10=0
        }
        return answer;
        
        /*
        참고할 풀이!
        문자열을 split로 하나씩 나눠서 비교하고 같은건 int로 변환해서 sum
        너무 신기하다....
        return Arrays.stream(String.valueOf(n).split("")).mapToInt(Integer::parseInt).sum();
        */
    }
}