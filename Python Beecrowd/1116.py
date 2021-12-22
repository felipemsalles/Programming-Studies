N = int(input())
count = 0
while count != N:
    x, y = map(int, input().split())
    if y == 0:
        print('divisao impossivel')
    if y != 0:
        divisao = x / y
        print('{:.1f}'.format(divisao))
    count += 1