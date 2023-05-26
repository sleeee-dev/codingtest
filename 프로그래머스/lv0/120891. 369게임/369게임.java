class Solution {
    public int solution(int order) {
        int answer = 0;
        String[] ord = String.valueOf(order).split("");
        
        for(int i=0;i<ord.length;i++){
            if((Integer.parseInt(ord[i])) == 0){ }
            else if((Integer.parseInt(ord[i])) % 3 == 0){
                answer++;
            }
        }
        return answer;
    }
}