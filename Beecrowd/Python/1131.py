vit_gremio = 0
vit_inter = 0
empate = 0
while True:
    inter, gremio = map(int, input().split())
    if inter == gremio:
        empate += 1
    else:
        if gremio > inter:
            vit_gremio += 1
        if inter > gremio:
            vit_inter += 1
    print('Novo grenal (1-sim 2-nao)')
    continuar = int(input())
    if continuar == 2:
        break


print('{} grenais'.format(vit_inter + vit_gremio))
print('Inter:{}'.format(vit_inter))
print('Gremio:{}'.format(vit_gremio))
print('Empates:{}'.format(empate))
if vit_inter > vit_gremio:
    print('Inter venceu mais')
elif vit_gremio > vit_inter:
    print('Gremio venceu mais')
elif vit_gremio == vit_inter:
    print('Nao houve vencedor')