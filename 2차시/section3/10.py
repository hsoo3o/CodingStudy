s = [list(map(int,input().split(' '))) for _ in range(9)]

def check(s):
    r = [0 for _ in range(9)]
    c = [0 for _ in range(9)]
    d1 = [0 for _ in range(9)]
    d2 = [0 for _ in range(9)]
    d3  = [0 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if r[s[i][j]-1] == 0 and c[s[j][i]-1] == 0:
                r[s[i][j]-1] = 1
                c[s[j][i]-1] = 1
                
            else:
                return "NO"

        r = [0 for _ in range(9)]
        c = [0 for _ in range(9)]
    for i in range(3):
        for k in range(3):
            if d1[s[i][k]-1] == 0:
                d1[s[i][k]-1] = 1
            else:
                return "NO"

        for k in range(3,6):
            if d2[s[i][k]-1] == 0:
                d2[s[i][k]-1] = 1
            else:
                return "NO"

        for k in range(6,9):
            if d3[s[i][k]-1] == 0:
                d3[s[i][k]-1] = 1
            else:
                return "NO"

        d1 = [0 for _ in range(9)]
        d2 = [0 for _ in range(9)] 
        d3 = [0 for _ in range(9)]
    return 'YES'       

print(check(s))
