X = int(input())
Y = int(input())
maior = X if X > Y else Y
menor = Y if Y < X else X
menor += 1
soma = 0
while menor < maior:
    if menor % 2 != 0:
        soma += menor
    menor += 1
print(soma)
