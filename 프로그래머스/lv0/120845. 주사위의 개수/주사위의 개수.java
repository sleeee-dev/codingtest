class Solution {
    public int solution(int[] box, int n) {
        int answer = 1;
        for(int i=0;i<box.length;i++){
            answer *= box[i]/n;
            }
        return answer;
    }
}


// 각 모서리의 길이를 정사각형 주사위 모서리 길이로 다 나눠서 곱하면 된다