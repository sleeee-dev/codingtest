class Solution {
    public int solution(String str1, String str2) {
        int answer = 0;
        int a = str1.indexOf(str2); //검색해서 단어가 없으면 -1반환 있으면 그 단어 반환
        
        if(a==-1){
            answer = 2;
            }
        else{
            answer = 1;
        }
        return answer;
    }
}