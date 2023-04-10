# 입력의 끝이 어딘지 분명하게 나와있지 않음 => 무한루프 + 예외처리가 필요함을 암시 
while True:
    try:
        A, B = map(int, input("").split())
        print(A+B)
    except:
        break