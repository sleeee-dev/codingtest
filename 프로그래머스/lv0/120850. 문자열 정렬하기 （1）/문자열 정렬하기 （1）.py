def solution(my_string):
    answer = []
    for i in my_string: # 문자열을 하나씩 나눠서 for문 돌리기
        if i.isdecimal(): # i가 0~9까지의 숫자인지 판별 => True라면
            answer.append(int(i)) # 해당하는 i를 int로 변환해서 answer에 추가
            answer.sort() # 오름차순 정렬
    return answer

# isdecimal() : 0~9의 숫자라면 True, 0~9의 숫자가 아니면 False
# isdigit(), isnumeric() : 숫자라면 True, 숫자가 아니면 False