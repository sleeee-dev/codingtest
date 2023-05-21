def solution(n):
    num = []
    answer = 0
    for i in range(4,n+1):
        for j in range(1,i+1):
            if i%j==0 :
                num.append(i)
                
        if num.count(i)>=3:
            answer+=1

    return answer

# n이하의 합성수 찾기
# num은 약수를 저장할 리스트
# i는 약수, j는 약수를 찾기 위한 변수
# 가장 작은 합성수가 4니까 4부터
# 약수를 찾아서 num에 저장
# count로 num에 저장된 약수가 3개 이상이면
# answer(합성수 개수)+=1 해서 합성수 개수 반환