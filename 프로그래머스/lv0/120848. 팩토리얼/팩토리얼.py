from math import factorial

def solution(n):
    k=10
    while n < factorial(k):
        k-=1
    return k

# 제한사항 0 < n ≤ 3,628,800
# 즉, 10! = 3,628,800 부터 factorial 시작
# n이 주어질 때, n < factorial(k) 을 만족하는 k값 출력