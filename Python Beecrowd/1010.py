# 1010
a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = float(c)

first_value = b * c

d, e, f = input().split(" ")
d = int(d)
e = int(e)
f = float(f)

second_value = e * f

total = first_value + second_value

print('VALOR A PAGAR: R$ %.2f' % total)

# VALOR A PAGAR (Portuguese) == TOTAL PRICE (English)