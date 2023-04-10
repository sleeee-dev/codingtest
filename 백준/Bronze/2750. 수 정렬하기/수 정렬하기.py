import sys

num_list=[]
n = int(sys.stdin.readline())
for i in range(n):
    num = int(sys.stdin.readline())
    num_list.append(num) # 입력 받은 수를 list에 이어붙임
    
num_list.sort() # 정렬 후 출력
for i in range(n):
  print(num_list[i])