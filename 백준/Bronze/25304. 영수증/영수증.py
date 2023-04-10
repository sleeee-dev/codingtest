X = int(input())
N = int(input())
sum = 0
for i in range(N):
    a, b = map(int, input().split())
    sum += a*b
if X == sum:
    print("Yes")
else:
    print("No")
# for i in N: 문자열 N을 하나씩 for문 돌리는것
# for i in range(N): 숫자 N까지의 범위 내에서 for문 돌리는것
# 변수 초기화 !!!!