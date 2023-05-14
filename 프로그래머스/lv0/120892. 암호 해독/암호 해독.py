def solution(cipher, code):
    return cipher[code-1::code]
# [start:stop:step] = [시작지점:종료지점:간격] : 빈칸으로 두면 맨앞,맨뒤,간격1 로 간주