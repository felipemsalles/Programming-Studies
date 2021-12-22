N = int(input())
count = 0
while N != count:
    n1, n2, n3 = input().split(" ")
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    media = (n1 * 2 + n2 * 3 + n3 * 5) / 10
    count += 1
    print('{:.1f}'.format(media))