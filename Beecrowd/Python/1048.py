salario = float(input())
if 0 <= salario <= 400.00:
    print('Novo salario: {:.2f}'.format(salario + (salario * 15/100)))
    print('Reajuste ganho: {:.2f}'.format((salario + (salario * 15/100) - salario)))
    print('Em percentual: 15 %')
elif 400.01 <= salario <= 800.00:
    print('Novo salario: {:.2f}'.format(salario + (salario * 12/100)))
    print('Reajuste ganho: {:.2f}'.format((salario + (salario * 12/100) - salario)))
    print('Em percentual: 12 %')
elif 800.01 <= salario <= 1200.00:
    print('Novo salario: {:.2f}'.format(salario + (salario * 10/100)))
    print('Reajuste ganho: {:.2f}'.format((salario + (salario * 10/100) - salario)))
    print('Em percentual: 10 %')
elif 1200.01 <= salario <= 2000.00:
    print('Novo salario: {:.2f}'.format(salario + (salario * 7/100)))
    print('Reajuste ganho: {:.2f}'.format((salario + (salario * 7/100) - salario)))
    print('Em percentual: 7 %')
elif salario > 2000.00:
    print('Novo salario: {:.2f}'.format(salario + (salario * 4/100)))
    print('Reajuste ganho: {:.2f}'.format((salario + (salario * 4/100) - salario)))
    print('Em percentual: 4 %')