import sys

word = sys.stdin.readline()
cnt = 1 # 10개씩 끊는것을 구분하기 위한 cnt 선언
for i in word:
  print(i, end="") # word를 for문 돌려서 하나식 출력 end="" <-붙여서 출력
  if cnt%10 == 0: # 10개씩 잘라서 줄바꿈
    print()
  cnt += 1 # i로 하나씩 출력이 될 때마다 cnt+1 해주면서 출력되는 글자수 카운트