def solution(n, k):
    answer = 0
    bonus = n//10
    k = k-bonus
    answer = n*12000 + k*2000
    return answer

# 1인분 12000원
# n인분 : n*12000
# 음료수 1개 2000원
# 음료수 k개 : k*2000
# 10인분 먹으면 음료수 1개 서비스
# n인분 k개
# if n<=10 :
# bonus = n//10
# k = k+bonus