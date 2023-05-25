class Solution {
    public int solution(int[] array) {
        for(int i=0;i<array.length;i++){
            for(int j=i;j<array.length;j++){
                if(array[i]>array[j]){ //array 값 비교해서 i보다 j가 크면 서로 값을 바꿈
                    int a = array[i];
                    array[i] = array[j];
                    array[j] = a; //값을 바꿈
                }//아니면 자리 안바꿈
            }
        }
        return array[array.length/2];
    }
}