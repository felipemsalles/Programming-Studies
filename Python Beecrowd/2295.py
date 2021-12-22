A, G, RA, RG = map(float, input().split())

rendimento_alcool = float(A / RA)
rendimento_gasolina = float(G / RG)

if rendimento_alcool < rendimento_gasolina:
    print('A')
else:
    print('G')