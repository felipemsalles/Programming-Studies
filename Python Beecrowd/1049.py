primeira = str(input()).lower()
segunda = str(input()).lower()
terceira = str(input()).lower()
if primeira == 'vertebrado':
    if segunda == 'ave':
        if terceira == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if terceira == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if segunda == 'inseto':
        if terceira == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if terceira == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')