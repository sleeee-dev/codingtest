class Solution {
    public int solution(String my_string) {
        String[] str = my_string.split(" ");
        int answer = Integer.parseInt(str[0]);
        //문자열을 쪼개고 숫자로 변환후 첫번째 숫자를 answer에 넣고
        //for문을 돌려서 + / - 구분에 따라 += / -= 연산하여 최종 answer값을 반환한다
        
        for(int i=1; i<str.length; i+=2){
            if(str[i].equals("+")){
                answer += Integer.parseInt(str[i+1]);
            } else {
                answer -= Integer.parseInt(str[i+1]);
            }
        }
        
        return answer;
    }
}