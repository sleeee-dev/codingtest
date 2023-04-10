import sys

sum = 0
for i in range(5):
  input = int(sys.stdin.readline())
  if input < 40:
    input = 40
  sum += input
print(int(sum/5))