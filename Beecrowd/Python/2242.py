linha = input()
vogais = ""

for letra in linha:

    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vogais += letra
if vogais == vogais[::-1]:
    print("S")
else:
    print("N")