import sys

while True:
    tri = list(map(int, sys.stdin.readline().split()))
    tri.sort() 
    
    if tri[0] == tri[1] == tri[2] == 0:
        break
    elif tri[2] ** 2 == tri[0] ** 2 + tri[1] ** 2:
        print("right")
    else:
        print("wrong")

# 피타고라스 정리 적용
# list로 입력받아서 정렬시키기
# 변수**2 : 제곱
