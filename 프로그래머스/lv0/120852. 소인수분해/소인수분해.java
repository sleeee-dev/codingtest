import java.util.ArrayList;

class Solution {
    public ArrayList solution(int n) {
        
        ArrayList answer = new ArrayList<>();

        for(int i=2; i<=n; i++) { 
            if(n % i == 0) {
                while(n % i == 0) {
                    n /= i;
                }
                answer.add(i);
            }
        }
        return answer;
    }
}

//ArrayList 사용
//n%i == 0일때, n이 i로 더 나눠지지 않을때까지 연산(2나 3 등의 인수가 여러번 반복될 경우)
//answer에 넣어서 반환