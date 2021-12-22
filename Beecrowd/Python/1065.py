# 1065
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
count = 0
pares = [n1, n2, n3, n4, n5]
for n in pares:
    if n % 2 == 0:
        count += 1
print("{} valores pares".format(count))