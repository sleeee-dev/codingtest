import sys

tot = []
for i in range(5):
  score = list(map(int, sys.stdin.readline().split())) # 점수 입력
  tot.append(sum(score)) # 총점 저장해서 append로 추가
print(tot.index(max(tot))+1, max(tot)) # 우승자, 점수 출력
# 인덱스는 0부터 시작이므로 최댓값의 인덱스+1 로 해야 몇번째 참가자인지 제대로 나옴