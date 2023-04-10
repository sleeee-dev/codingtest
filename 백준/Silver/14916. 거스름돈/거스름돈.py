import sys

n = int(sys.stdin.readline())
ans = 0

while True:
    if n%5 != 0:
        n -= 2 
        ans += 1
    else:
        ans += n//5 
        break
    
    if n < 0:
        break
        
if n < 0:
    print(-1)
else:
    print(ans)
    
    
# while문으로 일정한 조건에 도달할때까지 계속 반복시킴
# break로 빠져나가는 조건
# 1. n을 5로 나눈 나머지가 0이 될 때
# 2. n이 주어진 범위에 해당하지 않을때
# 5로 나눴을때 나머지가 0이 아니면 5로 딱떨어지는게 아니므로
# 먼저 2씩 빼면서 ans(거스름돈 개수) 하나씩 증가시키고
# 5로 나눴을때 나머지가 0이면 지금까지 쌓인 ans에 5로 나눈 몫을 더해서 break