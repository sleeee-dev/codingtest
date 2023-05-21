def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k))+1

# find() : 찾는 문자의 인덱스 반환 없으면 -1 반환
# index() : 찾는 문자의 인덱스 반환 없으면 에러
# 인덱스 반환이라 0부터 시작이니까 자릿수는 +1