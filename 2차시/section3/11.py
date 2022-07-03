from calendar import c


s = [list(map(int,input().split(' '))) for _ in range(7)]
cnt = 0

for i in range(7):
    r1,r2,c1,c2 = [],[],[],[]
    for j in range(2):
        r1.append(s[i][j])
        r2.append(s[i][4-j])

        c1.append(s[j][i])
        c2.append(s[4-j][i])
    if r1 == r2:
        cnt += 1
    if c1 == c2:
        cnt += 1

for i in range(7):
    r1,r2,c1,c2 = [],[],[],[]
    for j in range(1,3):
        r1.append(s[i][j])
        r2.append(s[i][6-j])

        c1.append(s[j][i])
        c2.append(s[6-j][i])
    if r1 == r2:
        cnt += 1
    if c1 == c2:
        cnt += 1

for i in range(7):
    r1,r2,c1,c2 = [],[],[],[]
    for j in range(2,4):
        r1.append(s[i][j])
        r2.append(s[i][8-j])

        c1.append(s[j][i])
        c2.append(s[8-j][i])
    if r1 == r2:
        cnt += 1
    if c1 == c2:
        cnt += 1

print(cnt)