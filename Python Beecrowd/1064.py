n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
listagem = [n1, n2, n3, n4, n5, n6]
count = 0
media = 0
for n in listagem:
    if n > 0:
        count += 1
        media += n
print('{} valores positivos'.format(count))
print('{:.1f}'.format(media/count))