class Solution {
    public int[] solution(int n) {
        int[] answer = new int[(n+1)/2];
        // 출력하려는 배열 크기 = 홀수갯수 = n/2인데 n이 홀수일 경우도 있으니 (n+1)/2
        for(int i=1;i<=n;i++){
            if((i%2)==1){
                answer[i/2] = i;
                //i는 n만큼 크기라서 배열 크기 안맞음 위에서 /2한거 맞춰주기
            }
        }
        return answer;
    }
}