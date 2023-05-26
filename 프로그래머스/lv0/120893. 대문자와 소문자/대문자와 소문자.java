class Solution {
    public String solution(String my_string) {
        String answer = "";
        char[] ch = my_string.toCharArray(); //String을 char배열로 바꾸기
        
        for(int i=0; i<ch.length;i++){
            ch[i] = (char)(ch[i] ^ 32); //아스키코드로 32씩 차이나서 이부분 XOR연산애서 반전시킴
        }
        answer = new String(ch); //char배열을 다시 String으로
        return answer;
    }
}

 /*
 ch[i] = (char)(ch[i] ^ 32);
 아스키 코드로 대소문자는 각각 32씩 차이나니까 이부분만 XOR 연산해서 반전시킴
 ^(XOR) : 같으면 0 다르면 1
 32는 2^5자리에서 1임을 나타냄
 그래서 32랑 XOR 연산했을때
 대문자라면 2^5 자리가 0이니까 0 XOR 1 = 1
 소문자라면 2^5 자리가 1이니까 1 XOR 1 = 0
 이렇게 2^5 자리가 0 <-> 1 변환이 되면 대소문자 변환이 됨
*/