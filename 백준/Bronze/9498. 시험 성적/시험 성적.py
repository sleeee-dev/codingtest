ans = int(input())
if ans >= 0 and ans <= 100:
    if ans >= 90 and ans <= 100:
        print("A")
    elif ans >= 80 and ans <= 89:
        print("B")
    elif ans >= 70 and ans <= 79:
        print("C")
    elif ans >= 60 and ans <= 69:
        print("D")
    else:
        print("F")