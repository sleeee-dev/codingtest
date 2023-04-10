# 메모리 제한 8MB, 시간제한 5초 
# 입력할때 sys.stdin.readline() 사용하기
# sort() 사용시 메모리 초과 됨
# 주어진 조건에서 N의 범위는 1<=N<=10000000이고
# N개의 입력은 10000보다 작거나 같은 자연수이다
# => N 개의 입력시 중복 가능함을 암시
# "계수정렬" 사용하기
# 배열 크기를 입력되는 수의 범위인 10001으로 지정하고(인덱스 시작이 0부터니까)
# 입력 받은 수를 각각의 수와 같은 인덱스값에 저장하고 정렬해서 뽑아내기
# ex) 5 입력시 인덱스 5에 저장 이런식으로

import sys

n = int(sys.stdin.readline())
num_list = [0]*10001

for i in range(n):
  num = int(sys.stdin.readline()) # 수를 입력받아 저장
  num_list[num] += 1 # 입력받은 수를 인덱스에 넣어서 그 수가 몇번씩 입력이 들어갔는지 카운트

for i in range(len(num_list)): # 배열 길이만큼 for문 돌리고
  if num_list[i] !=0: # 각 인덱스별로 카운트된 숫자가 0이 아니라면 입력된 숫자
    for j in range(num_list[i]): # 순서대로 출력하기 = 정렬이랑 같은 개념
      print(i)


# import sys

# n = int(sys.stdin.readline())
# num_list = []

# for i in range(n):
#   num_list.append(int(sys.stdin.readline())) #입력받아서 저장
  
# num_list.sort() # 정렬 => sort() 쓰면 메모리 초과로 걸림

# for i in num_list: # 출력
#   print(i)