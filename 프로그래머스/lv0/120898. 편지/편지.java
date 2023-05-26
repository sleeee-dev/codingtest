class Solution {
    public int solution(String message) {
        int answer = 0;
        String[] str = message.split("");
        answer = str.length * 2;
        return answer;
    }
}

/*
//굳이 배열에 나눠서 넣지 않고 그냥 String 길이로 해도 됨
class Solution {
    public int solution(String message) {
        return message.length()*2;
    }
}
*/