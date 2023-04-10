n = int(input())
sco = list(map(int, input().split()))
m = max(sco)
for i in range(n):
    sco[i] = sco[i]/m*100
print(sum(sco)/n)
# sum() : 합계 함수!
# sum = 0 으로 변수 선언해서 하는 방법도 있다
# n = int(input())
# sco = list(map(int, input().split()))
# m = max(sco)
# sum = 0
# for i in range(n):
#     sco[i] = sco[i]/m*100
#     sum += sco[i]
# result = sum/n
# print(result)