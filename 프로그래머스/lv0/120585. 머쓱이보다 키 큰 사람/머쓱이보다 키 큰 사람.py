def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)
    
    # height를 추가해서 내림차순정렬
    # height(머쓱이 키)의 인덱스값 == 머쓱이보다 키 큰 사람 수 (0부터 시작했으니까)
        
    
    # 처음풀이
    # answer = 0
    # for i in array:
    #     if i>height:
    #         answer +=1
    # return answer