def solution(numbers):
    numbers.sort()
    return numbers[-1]*numbers[-2]

# 풀이
# .sort() : 오름차순 정렬
# 맨 뒤에 두개가 가장 큰 값, 두번째로 큰 값이 됨
# 그 두 값을 곱해서 리턴