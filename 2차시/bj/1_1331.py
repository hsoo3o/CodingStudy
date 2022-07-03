import sys

check = [0 for _ in range(36)]
al = {'A':0,'B':6,'C':12,'D':18,'E':24,'F':30}

for _ in range(36):
    c = input()
    index = al[c[0]] + int(c[1])-1
    if check[index] != 1:
        check[index] = 1
    else:
        print('Invalid')
        break
else:
    print('Valid')
