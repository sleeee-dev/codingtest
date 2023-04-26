# 각자리수를 내림차순으로 정렬
# 첫째 줄에 정렬하려고 하는 수 N이 주어짐
# 내림차순으로 정렬 => 출력


import sys

n = list(map(str, sys.stdin.readline()))
n.sort(reverse=True)

for i in n:
    print(i, end='')
    
    
# 처음 풀이

# import sys

# n = int(sys.stdin.readline())

# num_list = []
# for i in str(n):
#   num_list.append(int(i))
  
# num_list.sort(reverse=True) # 내림차순 정렬 

# for i in num_list: # 출력
#    print(i, end='')