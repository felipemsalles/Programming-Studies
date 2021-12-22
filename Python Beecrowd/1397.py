N = 1

while N != 0:
    N = int(input())
    if N != 0:
        cont_a = cont_b = 0
        for i in range(N):
            a, b = map(int, input().split())
            if a > b:
                cont_a += 1
            elif b > a:
                cont_b += 1
        print('{} {}'.format(cont_a, cont_b))