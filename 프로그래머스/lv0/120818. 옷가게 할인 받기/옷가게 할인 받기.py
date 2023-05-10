def solution(price):
    answer = 0
    if 100000<=price<300000 :
        answer = 0.95*price
    elif 300000<=price<500000 :
        answer = 0.9*price
    elif price>=500000 :
        answer = 0.8*price
    else :
        answer = price
    return int(answer)