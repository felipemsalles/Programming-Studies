qtd_gasolina = qtd_disel = qtd_alcool = 0
while True:
    codigo = int(input())
    if codigo == 4:
        break
    if codigo == 1:
        qtd_alcool += 1
    if codigo == 2:
        qtd_gasolina += 1
    if codigo == 3:
        qtd_disel += 1

print('MUITO OBRIGADO')
print('Alcool: {}'.format(qtd_alcool))
print('Gasolina: {}'.format(qtd_gasolina))
print('Diesel: {}'.format(qtd_disel))