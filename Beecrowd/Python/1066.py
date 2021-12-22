# 1066
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
count_pares = count_impares = count_positivos = count_negativos = 0
listagem = [n1, n2, n3, n4, n5]

for n in listagem:
    if n % 2 == 0:
        count_pares += 1
    else:
        count_impares += 1

for n in listagem:
    if n > 0:
        count_positivos += 1
    elif n < 0:
        count_negativos += 1
print("{} valor(es) par(es)".format(count_pares))
print("{} valor(es) impar(es)".format(count_impares))
print("{} valor(es) positivo(s)".format(count_positivos))
print("{} valor(es) negativo(s)".format(count_negativos))