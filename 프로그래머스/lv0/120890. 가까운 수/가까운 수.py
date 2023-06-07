def solution(array, n):
    array.sort()
    answer = min(array, key=lambda x:abs(x-n))
    return answer


# min(key=) : key=조건 만족하는 최솟값
# lambda x: 익명함수, 자동리턴
# abs() : 인자로 전달된 숫자의 절대 값을 리턴
# 즉, abs(x-n) 이면 x-n 값이 음수여도 양수로 리턴된다
# min(array, key=lambda x:abs(x-n))
# array에서 abs(x-n)의 값이 가장 작은 수(즉 n과의 차이가 가장 적은 수=x) 리턴