

chess = [[0 for _ in range(6)] for _ in range(6)]
alph = ['A','B','C','D','E','F']
c = input()
prero = 6-int(c[1])
preco = alph.index(c[0])
onero = 6-int(c[1])
oneco = alph.index(c[0])
chess[prero][preco] = 1
for _ in range(35):
    c = input()
    ro = 6-int(c[1])
    co = alph.index(c[0])
    if abs(prero - ro) == 2 and abs(preco-co) == 1 and chess[ro][co] != 1:
        chess[prero][preco] = 1
    elif abs(preco-co) == 2 and abs(prero - ro) == 1 and chess[ro][co] != 1:
        chess[prero][preco] = 1
    else:
        print('Invalid')
        break
    prero,preco = ro,co
else:
    if abs(prero - onero) == 2 and abs(preco-oneco) == 1:
        print('Valid')
    elif abs(prero - onero) == 1 and abs(preco-oneco) == 2:
        print('Valid')

    else:
        print('Invalid')
