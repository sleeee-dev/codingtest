class Solution {
    public int solution(int n, int k) {
        return n * 12000 + k * 2000 - (n / 10 * 2000);
    }
}


//처음풀이
        // //양꼬치 n인분 , 음료수 k개
        // //=> 양꼬치 (n) 10인분당 음료수 +1 => k=k2+bonus
        // int answer = 0;
        // int bonus = 0;
        // int k2 = 0;
        // if(n>=10){
        //     bonus=n/10;
        //     k2=k-bonus;
        //     answer=(12000*n)+(2000*k2);
        // }else{
        //     answer=(12000*n)+(2000*k);
        // }
        // return answer;