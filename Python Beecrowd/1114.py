senha = 2002
while True:
    palpite = int(input())
    if palpite == senha:
        print('Acesso Permitido')
        break
    else:
        print('Senha Invalida')