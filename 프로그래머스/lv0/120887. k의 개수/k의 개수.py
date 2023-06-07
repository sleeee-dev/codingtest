def solution(i, j, k):
    answer = 0
    for i in range(i, j+1):
        answer += str(i).count(str(k))
    return answer

# a.count(b) : 문자열 a 안에 b가 몇번 들어갔는지 