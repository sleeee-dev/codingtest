import sys

mon = 1000 - int(sys.stdin.readline())
cnt = 0
while mon != 0:
  for i in [500, 100, 50, 10, 5, 1]:
    while mon >= i:
      mon -= i
      cnt += 1
print(cnt)