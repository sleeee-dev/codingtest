N, X = map(int, input().split())
A = [i for i in list(map(int, input().split())) if i < X]
for i in A:
    print(i, end=' ')

# 입력 받아서 for문 돌리고 X보다 작은 수만 A에 저장
# 한줄로 출력하는데 띄어쓰기 하나만 해서 출력.. 그냥 A 출력하면 리스트 형태라 [1, 4, 2, 3] 이렇게 나옴