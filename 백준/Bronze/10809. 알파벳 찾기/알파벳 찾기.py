str = input()
alph = list(range(97, 123))
for i in alph:
    print(str.find(chr(i)), end=' ')
# 아스키 코드로 알파벳 소문자 범위 지정한 리스트 생성후 (아스키코드 범위 97~122)
# alph 전체를 for문 돌려서 str 문자열 안에서 alph 각각의 문자가 처음 등장하는 위치를 반환
# find() : 문자열의 내부에 찾는 문자가 있으면 첫번째로 등장하는 위치를 반환 없으면 -1 반환
# ord("") : 문자열 -> 아스키코드
# chr() : 아스키코드 -> 문자열