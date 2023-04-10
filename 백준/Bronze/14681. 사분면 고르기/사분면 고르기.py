X = int(input())
Y = int(input())
if -1000 <= X <= 1000 and X != 0 and -1000 <= Y <= 1000 and Y != 0:
    if X > 0:
        print(1 if Y > 0 else 4)
    else:
        print(2 if Y > 0 else 3)