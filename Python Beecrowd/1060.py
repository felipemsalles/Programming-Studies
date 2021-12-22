# 1060
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
count = 0
listagem = [n1, n2, n3, n4, n5, n6]
for n in listagem:
    if n > 0:
        count += 1
print("{} valores positivos".format(count))