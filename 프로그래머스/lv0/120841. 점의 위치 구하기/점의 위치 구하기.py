def solution(dot):
    if dot[0]*dot[1]>0 :
        return 1 if dot[0]>0 else 3
    else :
        return 2 if dot[0]<0 else 4

    
    # 처음 풀었던 방법
    # answer = 0
    # if dot[0]>0 :
    #     if dot[1]>0 :
    #         answer=1
    #     else :
    #         answer=4
    # else :
    #     if dot[1]>0 :
    #         answer=2
    #     else :
    #         answer=3
    # return answer