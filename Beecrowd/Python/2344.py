N = int(input())
if 0 <= N <= 100:
    if 1 <= N <= 35:
        print('D')
    elif 36 <= N <= 60:
        print('C')
    elif 61 <= N <= 85:
        print('B')
    elif 86 <= N <= 100:
        print('A')
    else:
        print('E')