n = int(input())
for i in range(1, n+1):
    s = ' '*(n-i) + '*'*((2*i)-1)
    print(s)
# center() : 가운데정렬 그런데 가운데 정렬 쓰면 양쪽 여백이 생김 => 출려형식 오류
# 왼쪽에만 여백 생기면 됨
# ' '*(n-i) 로 여백주면 여백이 하나씩 줄어들어서 가운데정렬처럼 보이게 됨