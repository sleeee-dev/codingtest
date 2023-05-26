class Solution {
    public int[] solution(int n, int[] numlist) {
        int[] ans = new int[numlist.length];
        int j=0;
        for(int i=0;i<numlist.length;i++){
            if(numlist[i]%n == 0){
                ans[j] = numlist[i];
                j++;
            }
        }
        //여기까지 하면 길이를 numlist에 맞춰서 했기때문에 n의 배수 값 넣고 남은 값들은 다 0으로 들어가서 최종값은 이걸 다 빼고 새로 배열 만들어야함
        int[] answer = new int[j];
        for(int i=0;i<j;i++){
            if(ans[i] != 0){
                answer[i] = ans[i];
            }
        }
        return answer;
    }
}