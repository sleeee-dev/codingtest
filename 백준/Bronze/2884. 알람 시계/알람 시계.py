h, m = list(map(int, input().split()))

if m >= 45:
  print(h, m-45)
elif m < 45:
  h = h-1
  if h < 0:
    print(h+24, m+15)
  else:
    print(h, m+15)

# 처음에 이렇게 짜고 위 코드로 개선함
# m = m - 45
# if m < 0:
#   m = m + 60
#   h = h - 1
#   if h < 0:
#     h = h + 24
# elif m >= 60 :
#   m = m - 60
#   h = h + 1
#   if h >= 24 :
#     h = h - 24
# print(h, m)