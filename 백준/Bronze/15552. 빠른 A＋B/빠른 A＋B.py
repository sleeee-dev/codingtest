# 시간초과를 방지하기 위해
# import sys
# input = sys.stdin.readline
# 다음과 같이 선언하고 사용하는 연습하기

import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
  a, b = list(map(int, input().split()))
  print(a+b)