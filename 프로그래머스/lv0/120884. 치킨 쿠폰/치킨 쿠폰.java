class Solution {
    public int solution(int chicken) {
        int answer = 0;

        while (chicken >= 10) {
            int chickenCoupon = chicken / 10; //치킨쿠폰 발급
            int restCoupon = chicken % 10; //남은 쿠폰수
            chicken = chickenCoupon + restCoupon;

            answer += chickenCoupon;
        }

        return answer;
    }
}