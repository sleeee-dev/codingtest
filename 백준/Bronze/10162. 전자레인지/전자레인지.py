import sys

s = int(sys.stdin.readline())

# 5분,1분,10초로 표현할 수 없음 == 10으로 나눠지지 않는 경우
if s%10 != 0 :
  print(-1)
else :
  for i in [300, 60, 10] :
    print(s//i, end=' ') # s//i : s를 i로 나는 몫
    s = s%i # s%i : s를 i로 나눈 나머지