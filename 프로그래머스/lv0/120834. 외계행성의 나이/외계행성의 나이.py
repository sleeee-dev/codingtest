def solution(age):
    return ''.join(chr(int(i)+97) for i in str(age))

# chr() : 아스키코드를 문자열로
# ord() : 문자열를 아스키코드로
# age 한글자씩 나눠야하니까 문자열로 바꿔서 for돌리고 각각 숫자로 바꾼후에 거기에 해당하는 문자열 출력해서 붙이기
# 아스키코드 A = 65 , a = 97