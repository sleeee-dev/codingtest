class Solution {
    public String[] solution(String my_str, int n) {
        
        //주어진 문자열의 길이가 n으로 딱 떨어지지 않을때는 나머지+1 한값으로 마지막 배열에 저장
        int size = my_str.length()/n;
        if(my_str.length() % n != 0){
            size++;
        }
        
        String[] answer = new String[size];
        int index = 0;
        for(int i = 0; i < my_str.length(); ){
            int next = Math.min(i+n,my_str.length());
            answer[index] = my_str.substring(i,next);
            i += n;
            index++;
        }
        return answer;
    }
}