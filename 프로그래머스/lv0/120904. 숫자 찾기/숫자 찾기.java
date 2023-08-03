class Solution {
    public int solution(int num, int k) {
        int answer = -1;
        String sNum[] = String.valueOf(num).split("");
        //num을 String으로 변환 후 split => 배열로 저장
		for(int i=0; i<sNum.length; i++) {
			if(sNum[i].equals(String.valueOf(k))) {
				answer = i+1; //i가 index값이므로 +1 해주기
				break;  
            }
		}
        return answer;
    }
}