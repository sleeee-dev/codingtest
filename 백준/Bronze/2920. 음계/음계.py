c_list = list(map(int, input().split())) # 입력, split, int형변환, 리스트로 저장
if (c_list == sorted(c_list, reverse=False)): # sorted(정렬하려는리스트, 정렬기준) 
    print("ascending")
elif (c_list == sorted(c_list, reverse=True)):
    print("descending")
else:
    print("mixed")

# sort() : 주어진 리스트를 정렬 (기존 리스트가 정렬되어서 변함)
# sorted() : 주어진 리스트를 정렬해서 새로운 리스트로 반환 (새 리스트가 반환되므로 기존 리스트는 변하지X)