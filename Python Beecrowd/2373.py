N = int(input())
qnt_copos = 0
for i in range(1, N + 1):
    L, C = map(int, input().split())
    if L > C:
        qnt_copos += C
print(qnt_copos)