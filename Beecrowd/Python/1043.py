A, B, C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)
Area = (A + B) * C / 2
Perimetro = A + B + C
if abs(B - C) < A < (B + C) and (A - C) < B < (A + C) and (A - B) < C < (A + B):
    print('Perimetro = {:.1f}'.format(Perimetro))
else:
    print('Area = {:.1f}'.format(Area))