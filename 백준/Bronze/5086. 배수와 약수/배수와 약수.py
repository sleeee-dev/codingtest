import sys

while True:
  n1, n2 = list(map(int,sys.stdin.readline().split()))

  if n1 == n2 == 0 :
    break;
  elif n1 % n2 == 0:
    print("multiple")
  elif n2 % n1 == 0:
    print("factor")
  else:
    print("neither")