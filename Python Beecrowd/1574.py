test = int(input())
for i in range(0, test):
    count = 0
    lista = []
    test_1 = int(input())

    for i in range(0, test_1):
        lista.append(input())

    for j in range(0, test_1):
        if lista[j] == 'LEFT':
            count = count-1
        elif lista[j] == 'RIGHT':
            count = count+1
        else:
            lista[j] = lista[j].split()
            lista[j] = lista[j][len(lista[j])-1]
            lista[j] = lista[int(lista[j])-1]
            if lista[j] == 'LEFT':
                count -= 1
            else:
                count += 1
    print(count)