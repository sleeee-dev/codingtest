import sys

num = list(map(int, sys.stdin.readline().split()))
# 리스트로 받으면 [3, 1, 2] 이런 형식으로 들어오게 되므로 이대로 정렬해서 출력하면 틀림

# 정렬 두가지 다 가능 sort는 기존 리스트 자체를 정렬, sorted는 새로운 리스트에 정렬한것 저장
# num = sorted(num)
num.sort()

for i in num:
  print(i, end=" ")