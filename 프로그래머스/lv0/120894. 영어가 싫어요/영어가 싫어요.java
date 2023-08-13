class Solution {
    public long solution(String numbers) {
        //numbers를 배열로 지정 numArr[0] = "zero" 이런식으로
        String[] numArr = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        
        //numArr를 for문 돌려서 numbers의 문자와 numArr 배열값과 비교해서 해당 index 숫자로 치환하기
        for (int i = 0; i < numArr.length; i++) {
            numbers = numbers.replaceAll(numArr[i], String.valueOf(i));
        }
        return Long.parseLong(numbers);
    }
}