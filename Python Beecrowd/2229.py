t = 1
pedaços = int(input())
while pedaços != -1:
    ant, atual = 2, 2
    for m in range(pedaços):
        atual = 2 * ant - 1
        ant = atual
    print('Teste', t)
    print(atual**2)
    print()
    t += 1
    pedaços = int(input())
