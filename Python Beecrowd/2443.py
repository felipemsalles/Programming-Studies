a, b, c, d = map(int, input().split())
numerador = a * d + c * b
denominador = b * d
resto = a % b
a, b, c, d = map(int, input().split())


def mdc(b, d):
    if d == 0:
        return b
    return mdc(d, b % d)


def mmc(b, d):
    print(abs(b*d) / mdc(b, d))