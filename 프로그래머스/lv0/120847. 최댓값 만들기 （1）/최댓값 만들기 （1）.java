class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        int max1=0;//가장 큰 수
        int max2=0;//두번째로 큰 수
        int index=0;
        
        for(int i=0;i<numbers.length;i++){
            if(numbers[i]>max1){
                max1=numbers[i];
                index = i; //가장 큰 수의 인덱스 값을 저장
            }                
        }
        for(int j=0;j<numbers.length;j++){
            if(j!=index && numbers[j]>max2){
                max2=numbers[j];
            }
        }
        answer = max1*max2;
        return answer;
    }
}

/*
        for(int j=0;j<numbers.length;j++){
            if(max1>numbers[j] && numbers[j]>max2){
                max2=numbers[j];
            }
        }
처음에 구했던 방식은 가장 큰 숫자를 max1에 두고
두번째로 큰 숫자를 max2로 두고 계산하는 방식이었는데
이 경우, 같은 숫자가 반복해서 나왔을때 올바르게 체크 되지 않아서 오류가 생김
즉, 같은 숫자가 반복되면 max1과 max2의 값이 같아야하는데 이게 안됨
그래서 가장 큰 수의 인덱스값을 저장하고,
그 인덱스를 제외한 수 중에서 다음으로 큰 수를 구하는걸로 하면
max1과 max2가 같은 경우에도 계산이 가능해짐
*/