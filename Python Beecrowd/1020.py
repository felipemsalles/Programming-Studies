# 1020
idade = int(input())
anos = int(idade / 365)
saldo = idade - anos * 365

meses = int(saldo / 30)
dias = saldo - meses * 30
print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))