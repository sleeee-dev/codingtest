N = int(input())
if 0 < N <= 100000:
    for i in range(N, 0, -1):
        print(i)
# for i in range(N, 0, -1): 범위는 N을 시작으로 0까지 -1 간격으로 for문 돌리고 그 값이 i로 출력