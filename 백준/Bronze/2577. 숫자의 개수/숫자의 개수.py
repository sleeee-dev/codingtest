import sys

res = 1
for i in range(3):
  input = int(sys.stdin.readline())
  res *= input

for i in range(10):
  print(str(res).count(str(i)))

# for문으로 0~9까지 반복
# res를 형변환 해서 0~9까지 count 사용
# 문자열.count(특정문자) 문자열 내에서 특정 문자의 반복횟수를 찾아주는 함수
# count 함수를 쓰기 위해 res, i 둘 다 str로 형변환 해주어야 함 