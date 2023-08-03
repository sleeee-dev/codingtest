class Solution {
    public int solution(String my_string) {
        String[] strArr = my_string.split("[^0-9]");
        //정규식 사용.
        //연속된 숫자는 하나의 숫자로 간주 => 숫자가 아닐때를 기준으로 split
        //숫자가 아닌 경우 공백이 생기므로 0으로 return => isEmpty로 구분
        int answer = 0;

        for (String value : strArr) {
            answer += value.isEmpty() ? 0 : Integer.parseInt(value);
        }
        return answer;
    }
}