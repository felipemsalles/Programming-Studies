casototal = int(input())

for i in range(casototal):
	texto1 = input().split(" ")
	texto2 = []
	texto3 = []
	for x in texto1:
		if x != "":
			texto2.append(x)
	for y in texto2:
		texto3.append(y[0])
	print(''.join(texto3))