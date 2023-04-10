N = int(input())
if 1 <= N <= 100:
    for i in range(1, N+1):
        s = '*'*i
        print(s.rjust(N))
        
# rjust(n,'s') : 전체 길이 n 중 오른쪽 정렬 , s는 공백을 대체할 문자 없으면 공백 그대로 출력
# ljust(n,'s') : 왼쪽 정렬
# zfill(n) : 전체 길이 n 중에 해당 문자를 제외한 나머지 공백을 0을 왼쪽에 채워줌