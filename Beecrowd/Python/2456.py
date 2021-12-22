c1, c2, c3, c4, c5 = map(int, input().split())

cartas = [c1, c2, c3, c4, c5]

if cartas == sorted(cartas):
    print('C')
elif cartas == sorted(cartas, reverse=True):
    print('D')
else:
    print('N')



