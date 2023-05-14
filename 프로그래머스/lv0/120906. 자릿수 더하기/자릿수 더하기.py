def solution(n):
    return sum(int(i) for i in str(n))


    # 처음 풀이
    # answer = 0
    # while n>0:
    #     answer += n%10
    #     n = n//10
    # return answer