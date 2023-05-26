import java.util.Arrays;

class Solution {
    public int[] solution(String my_string) {
        
        String[] str = my_string.replaceAll("[^0-9]","").split(""); // 0-0가 아니면 공백으로 치환해서 split
        Arrays.sort(str); // 오름차순 정렬
        
        int[] answer = new int[str.length]; // answer 배열 선언 길이!!!
        for(int i=0;i<answer.length;i++){
            answer[i] = Integer.parseInt(str[i]); //int 형변환!!
        }
        return answer;
    }
}