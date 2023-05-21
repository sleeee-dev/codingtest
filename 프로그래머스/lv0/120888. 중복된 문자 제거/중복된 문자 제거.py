def solution(my_string):
    return ''.join(dict.fromkeys(my_string))
    
# dict.fromkeys(key,value) : 리스트 중복 제거시 사용가능 => 공부 더 하기

# cf.return ''.join(list(set(my_string))) : 중복 삭제는 되지만 순서가 없어서 결과가 달라짐


# 처음 푼 풀이
# def solution(my_string):
#     answer = ''
#     for i in my_string:
#         if i not in answer:
#             answer+=i
#     return answer