# 반복문으로 print 출력할때, end='' 옵션 넣으면 여러줄을 다 붙여서 출력함
T = int(input())
for i in range(T):
    R, S = input().split()
    S2 = len(S)
    for i in range(S2):
        print(S[i]*int(R), end='')
    print()