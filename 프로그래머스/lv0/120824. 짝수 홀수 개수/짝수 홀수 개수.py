def solution(num_list):
    answer = [0,0]
    for i in num_list:
        answer[i%2] +=1
    return answer

# answer = [0,0] : answer[0] = 0, answer[1] = 0 으로 초기화 되어있는것을 의미
# for i in num_list:
#   answer[i%2] +=1
# for문으로 num_list요소들을 돌려가며 answer에 넣고 각각 2로 나눈 나머지 찾기
# 2로 나눈 나머지는 0이나 1 두개만 나옴
# 즉, for문을 돌리면 answer[0] 이나 answer[1] 두가지로 나온다는것
# 여기에서 answer[0] 이 나오면 +1이 되고
# answer[1] 이 나오면 +1이 되는 식으로 카운트 할 수 있음