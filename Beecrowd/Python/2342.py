N = int(input())
P, C, Q = map(str, input().split(" "))
P = int(P)
C = str(C)
Q = int(Q)
if C == "+":
    calculo = P + Q
    if (P + Q) <= N:
        print('OK')
    else:
        print('OVERFLOW')

else:
    calculo = P * Q
    if (P * Q) <= N:
        print('OK')
    else:
        print('OVERFLOW')


