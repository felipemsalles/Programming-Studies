while True:
    L, R = map(int, input().split())
    if L == 0 and R == 0:
        break
    else:
        print(L + R)