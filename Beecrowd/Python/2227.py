teste = 1
while True:
    a, v = [int(i) for i in input().split()]
    if a == v == 0:
        break

    aeroporto = [0] * a
    while v:
        v -= 1
        x, y = [int(i) for i in input().split()]
        aeroporto[x-1] += 1
        aeroporto[y-1] += 1

    m = max(aeroporto)
    maior = [str(i + 1) for i in range(len(aeroporto)) if aeroporto[i] == m]
    print(f'Teste {teste}')
    teste += 1
    print(' '.join(maior), '')
    print()