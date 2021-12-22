teste = 1
while True:
    valor = int(input())
    if valor == 0:
        break
    bits = ['0'] * 4
    if valor >= 50:
        bits[0] = str(valor // 50)
        valor %= 50
    if valor >= 10:
        bits[1] = str(valor // 10)
        valor %= 10
    if valor >= 5:
        bits[2] = str(valor // 5)
        valor %= 5
    bits[3] = str(valor)
    print(f'Teste {teste}')
    print(' '.join(bits))
    print()
    teste += 1