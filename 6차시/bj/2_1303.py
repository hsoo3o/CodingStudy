import sys

def findw(i,j):
    global w
    if i > m or j > n:
        return
    else:
        if not ch[i][j+1] and war[i][j+1] =='W':
            ch[i][j+1] = 1
            w += 1
            findw(i,j+1)
        if not ch[i][j-1] and war[i][j-1] =='W':
            ch[i][j-1] = 1
            w += 1
            findw(i,j-1)
        if not ch[i-1][j] and war[i-1][j] =='W':
            ch[i-1][j] = 1
            w += 1
            findw(i-1,j)
        
        if not ch[i+1][j] and war[i+1][j] =='W':
            ch[i+1][j] = 1
            w += 1
            findw(i+1,j)
        else:
            return


def findb(i,j):
    global b
    if i > m or j > n:
        return
    else:    
        if not ch[i-1][j] and war[i-1][j] =='B':
            ch[i-1][j] = 1
            b += 1
            findb(i-1,j)
        if not ch[i+1][j] and war[i+1][j] =='B':
            ch[i+1][j] = 1
            b += 1
            findb(i+1,j)
        if not ch[i][j+1] and war[i][j+1] =='B':
            ch[i][j+1] = 1
            b += 1
            findb(i,j+1)
        if not ch[i][j-1] and war[i][j-1] =='B':
            ch[i][j-1] = 1
            b += 1
            findb(i,j-1) 
        else:
            return


n,m = map(int, sys.stdin.readline().split())
war = []
ch = [[0 for _ in range(n+2)] for _ in range(m+2)]
n_ans,m_ans = 0,0
for i in range(m):
    war.append([0]+list(sys.stdin.readline().rstrip())+[0])
war.append([0]*(n+2))
war.insert(0,[0]*(n+2))

for i in range(m+1):
    for j in range(n+1):
        w,b = 1,1
        if war[i][j] =='W' and not ch[i][j]:
            ch[i][j] = 1
            findw(i,j)
            n_ans += w**2
        if war[i][j] =='B' and not ch[i][j]:
            ch[i][j] = 1
            findb(i,j)
            m_ans += b**2

print(str(n_ans)+' '+str(m_ans))

