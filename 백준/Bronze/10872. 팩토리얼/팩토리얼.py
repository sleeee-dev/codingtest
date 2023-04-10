def fact(i):
    if i == 0:
        return 1
    return i*fact(i-1)

N = int(input())
print(fact(N))