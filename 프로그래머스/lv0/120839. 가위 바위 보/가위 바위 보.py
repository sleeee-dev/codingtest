def solution(rsp):
    answer = {'2':'0', '0':'5', '5':'2'}
    return ''.join(answer[i] for i in rsp)

# 딕셔너리 key==value 형태로 만들기
# rsp가 key니까 해당하는 value값 출력
# answer.get(key) 이렇게 value 값 출력할 수도 있음