def solution(n):
    return len([i for i in range(1,n+1) if n%i ==0])

# 순서쌍의 개수 == 약수의 개수
# 20의 약수
# 1,2,4,5,10,20 6개
# 약수는 어떻게 구하지?
# for 돌려서 % 나머지가 0인 수

# 처음 풀이
# def solution(n):
#     answer = 0
#     for i in range(1,n+1):
#         if n%i==0:
#             answer +=1
#     return answer