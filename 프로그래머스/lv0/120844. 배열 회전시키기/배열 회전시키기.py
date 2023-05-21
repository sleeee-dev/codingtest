def solution(numbers, direction):
    answer = []
    return [numbers[-1]] + numbers[:-1] if direction=="right" else numbers[1:] + [numbers[0]]


# deque 활용 공부해보기