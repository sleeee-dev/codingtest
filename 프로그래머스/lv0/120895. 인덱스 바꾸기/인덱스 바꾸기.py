def solution(my_string, num1, num2):
    my_string = list(my_string)
    my_string[num1],my_string[num2] = my_string[num2], my_string[num1]
    return ''.join(my_string)

# list로 변환후 인덱스 바꾸고 붙여서 출력