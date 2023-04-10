h, m = list(map(int, input().split()))
c = int(input())

h += c // 60 # //연산자 : 나머지
m += c % 60  # % 연산자 : 몫

if m >= 60:
  h += 1
  m -= 60
if h >= 24:
  h -= 24
print(h,m)
    