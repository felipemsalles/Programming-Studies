# 1013
a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

maiorAB = (a + b + abs(a-b)) / 2
if c > maiorAB:
    print(c, 'eh o maior')
else:
    print('%.0f' % maiorAB, 'eh o maior')



# 'eh o maior' (informal way in Portuguese to say that a number is the largest number)