# 한줄로 전체 입력 받아서 나누는 것 vs 한줄마다 하나의 값 받아서 나누는 것 구분하기
# 처음에 리스트 초기화가 필요
num_list = []
for i in range(9):
    num_list.append(int(input()))
m = max(num_list)
print(m)
print(num_list.index(m)+1)